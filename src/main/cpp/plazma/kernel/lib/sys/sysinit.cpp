
#include <iostream>
#include "sysinit.h" // importatnt before OS_<NAME> detection
#include "sysexec.h"

#ifdef OS_WIN
#include <io.h>
#include <windows.h>

#include <shlobj.h>
#include <objidl.h>
//#include <stdlib.h>
#include <Wincon.h>

#define PROPSIZE 9      // eight-letter + null terminator
#define SNAMESIZE 86    // max number of chars for LOCALE_SNAME is 85

#include <locale.h>
#include <sys/types.h>
#include <sys/timeb.h>

#else
#include <unistd.h>
#include <dlfcn.h>

#include <sys/utsname.h>        /* For os_name and os_version */
//#include <langinfo.h>         /* For nl_langinfo */
//#include <locale.h>
#include <pwd.h>
#endif

#ifdef _ALLBSD_SOURCE
#ifndef P_tmpdir
#include <paths.h>
#define P_tmpdir _PATH_VARTMP
#endif
#endif

#ifndef P_tmpdir
#define P_tmpdir "/var/tmp"
#endif

#ifdef OS_MAC

#ifdef OS_MAC_FRAMEWORK
#include <CoreFoundation/CoreFoundation.h>
#include <CoreServices/CoreServices.h>
#endif

#endif


#include "plazma/kernel/lib/str/strlib.h"

namespace syslib {



//// MACOS ////

#ifdef OS_MAC

#ifdef OS_MAC_FRAMEWORK
const char* getLocaleValue(CFLocaleRef locale, CFLocaleKey key) {
  CFStringRef value = (CFStringRef) CFLocaleGetValue(locale, key); 
  const char* ch = CFStringGetCStringPtr(value, kCFStringEncodingUTF8);
  if (ch == nullptr) {
    return nullptr;
  }
  return ch;
}

Locale* loadLocaleMac() {

  CFLocaleRef cflocale = CFLocaleCopyCurrent();

  const char* name = getLocaleValue(cflocale, kCFLocaleIdentifier);

  const char* language = getLocaleValue(cflocale, kCFLocaleLanguageCode);
  const char* script = getLocaleValue(cflocale, kCFLocaleScriptCode);
  const char* country = getLocaleValue(cflocale, kCFLocaleCountryCode);  
  const char* variant = getLocaleValue(cflocale, kCFLocaleVariantCode);

  //CFStringRef identifier = CFLocaleGetIdentifier(cflocale);
  //const char* ch = CFStringGetCStringPtr(identifier, kCFStringEncodingUTF8);

  CFRelease(cflocale);

  if (name == nullptr) {
    return nullptr;
  }

  Locale* result = new Locale();
  result->name = strdup(name);
  
  if (language != nullptr) {
    result->language = strdup(language);
  }
  if (script != nullptr) {
    result->script = strdup(script);
  }
  if (country != nullptr) {
    result->country = strdup(country);
  }
  if (variant != nullptr) {
    result->variant = strdup(variant);
  }

  return result;


}

void initLocaleMac_F(SysInfo& sysInfo) {

  Locale* posixLocale = nullptr; // For loading encoding
  Locale* formatLocale = loadLocaleMac(); // TODO: LC_CTYPE
  if (formatLocale == nullptr) {
    formatLocale = loadLocale(LC_CTYPE);
    posixLocale = formatLocale;
  } 
  initLocale(sysInfo, LC_CTYPE, formatLocale);

  Locale* displayLocale = loadLocaleMac(); // TODO: LC_MESSAGES
  if (displayLocale == nullptr) {
    displayLocale = loadLocale(LC_MESSAGES);
  } 
  initLocale(sysInfo, LC_MESSAGES, displayLocale);

  if (posixLocale == nullptr) {
    posixLocale = loadLocale(LC_CTYPE);
    
  }

  char* encoding = nullptr;
  if (posixLocale != nullptr) {
    encoding = posixLocale->encoding;    
  }

  if (encoding != nullptr) {
    sysInfo.encoding = strdup(encoding);
  }

  if (formatLocale != nullptr) {
    delete formatLocale;

  }

  if (displayLocale != nullptr) {
    delete displayLocale;
  }

}

#endif // OS_MAC_FRAMEWORK

// ALTERNATIVE
void initLocaleMac_A(SysInfo& sysInfo) {
    initLocalePosix(sysInfo);
}

void initLocaleMac(SysInfo& sysInfo) {
  #ifdef OS_MAC_FRAMEWORK

  #ifdef OS_MAC_FRAMEWORK_LOCALE
  initLocaleMac_F(sysInfo);
  #else
  initLocaleMac_A(sysInfo);
  #endif

  #else
  initLocaleMac_A(sysInfo);
  #endif
}

#ifdef OS_MAC_FRAMEWORK
void initOsMac_F(SysInfo& sysInfo) {

    SInt32 majorVersion = 0;
    SInt32 minorVersion = 0;
    SInt32 bugFixVersion = 0;

    Gestalt(gestaltSystemVersionMajor, &majorVersion);
    Gestalt(gestaltSystemVersionMinor, &minorVersion);
    Gestalt(gestaltSystemVersionBugFix, &bugFixVersion);

    std::string version = "" + std::to_string(majorVersion) + "." + std::to_string(minorVersion) + "." + std::to_string(bugFixVersion);

    sysInfo.os_name = "Mac OS X";
    sysInfo.os_version = strdup(version.c_str());   
}
#endif // OS_MAC_FRAMEWORK

// UTILS: getSuffix(prefix)
std::string getLineValue(const std::string& name, const std::string& line) {
    if (name.empty() || line.empty()) {
        return "";
    }
    std::string value = line.substr(name.length());
    strlib::_trimAll(value);
    return value;
}

// ALTERNATIVE
void initOsMac_A(SysInfo& sysInfo) {
    
       std::string cmd = "sw_vers";
       std::string info = exec(cmd.c_str(), true);
       if (info.empty()) {
         return;
       }

       std::vector<std::string> lines = strlib::split(info, '\n');
       int size = lines.size();

       const std::string PRODUCT_NAME = "ProductName:";
       const std::string PRODUCT_VERSION = "ProductVersion:";
       //const std::string BUILD_VERSION = "BuildVersion:";

       std::string line;
       std::string value;

       for (int i = 0; i < size; i++) {
         line = lines[i];
         if (strlib::startsWith(line, PRODUCT_NAME)) {
           value = getLineValue(PRODUCT_NAME, line);
           sysInfo.os_name = strdup(value.c_str());
         } else if (strlib::startsWith(line, PRODUCT_VERSION)) {
           value = getLineValue(PRODUCT_VERSION, line);
           sysInfo.os_version = strdup(value.c_str());
         }
         // else if (strlib::startsWith(line, BUILD_VERSION)) {
         //  value = getLineValue(BUILD_VERSION, line);
         //  sysInfo.os_build = strdup(value.c_str());
         //}
       }

       //ProductName    :	Mac OS X
       //ProductVersion :	10.14.6
       //BuildVersion   :	18G95
}

void initOsMac(SysInfo& sysInfo) {
    #ifdef OS_MAC_FRAMEWORK

    #ifdef OS_MAC_FRAMEWORK_SYSTEM
    initOsMac_F(sysInfo);
    #else
    initOsMac_A(sysInfo);
    #endif

    #else
    initOsMac_A(sysInfo);
    #endif  
}

#endif // OS_MAC


//// WIN ////

#ifdef OS_WIN

typedef struct {

  int majorVersion = 0;
  int minorVersion = 0;
  int buildNumber = 0;

  boolean is_workstation;
  boolean is_64bit;
  DWORD platformId;

} VersionInfo;

/*
 * From msdn page on OSVERSIONINFOEX, current as of this
 * writing, decoding of dwMajorVersion and dwMinorVersion.
 *
 *  Operating system            dwMajorVersion  dwMinorVersion
 * ==================           ==============  ==============
 *
 * Windows 95                   4               0
 * Windows 98                   4               10
 * Windows ME                   4               90
 * Windows 3.51                 3               51
 * Windows NT 4.0               4               0
 * Windows 2000                 5               0
 * Windows XP 32 bit            5               1
 * Windows Server 2003 family   5               2
 * Windows XP 64 bit            5               2
 *       where ((&ver.wServicePackMinor) + 2) = 1
 *       and  si.wProcessorArchitecture = 9
 * Windows Vista family         6               0  (VER_NT_WORKSTATION)
 * Windows Server 2008          6               0  (!VER_NT_WORKSTATION)
 * Windows 7                    6               1  (VER_NT_WORKSTATION)
 * Windows Server 2008 R2       6               1  (!VER_NT_WORKSTATION)
 * Windows 8                    6               2  (VER_NT_WORKSTATION)
 * Windows Server 2012          6               2  (!VER_NT_WORKSTATION)
 * Windows Server 2012 R2       6               3  (!VER_NT_WORKSTATION)
 * Windows 10                   10              0  (VER_NT_WORKSTATION)
 * Windows 11                   10              0  (VER_NT_WORKSTATION)
 *       where (buildNumber >= 22000)
 * Windows Server 2016          10              0  (!VER_NT_WORKSTATION)
 * Windows Server 2019          10              0  (!VER_NT_WORKSTATION)
 *       where (buildNumber > 17762)
 * Windows Server 2022          10              0  (!VER_NT_WORKSTATION)
 *       where (buildNumber > 20347)
 *
 * This mapping will presumably be augmented as new Windows
 * versions are released.
 */

char* getWIN32_WINDOWS_Name(VersionInfo ver) {
  if (ver.majorVersion == 4) {
    switch (ver.minorVersion) {
      case  0: return "Windows 95";
      case 10: return "Windows 98";
      case 90: return "Windows Me";
    }
    return "Windows 9X (unknown)";
   }
   return "Windows 9X (unknown)"; 
}

char* getWIN32_NT_5_Name(VersionInfo ver) {
  switch (ver.minorVersion) {
    case  0: return "Windows 2000";
    case  1: return "Windows XP";
    case  2:
        /*
         * From MSDN OSVERSIONINFOEX and SYSTEM_INFO documentation:
         *
         * "Because the version numbers for Windows Server 2003
         * and Windows XP 6u4 bit are identical, you must also test
         * whether the wProductType member is VER_NT_WORKSTATION.
         * and si.wProcessorArchitecture is
         * PROCESSOR_ARCHITECTURE_AMD64 (which is 9)
         * If it is, the operating system is Windows XP 64 bit;
         * otherwise, it is Windows Server 2003."
         */
         if (ver.is_workstation && ver.is_64bit) {
            return "Windows XP"; /* 64 bit */
         } else {
             return "Windows 2003";
         }

  }
  return "Windows NT (unknown)"; 
}

char* getWIN32_NT_6_Name(VersionInfo ver) {
  /*
   * See table in MSDN OSVERSIONINFOEX documentation.
   */
   if (ver.is_workstation) {
        switch (ver.minorVersion) {
            case  0: return "Windows Vista";
            case  1: return "Windows 7";
            case  2: return "Windows 8";
            case  3: return "Windows 8.1";
          }
    } else {
        switch (ver.minorVersion) {
            case  0: return "Windows Server 2008";
            case  1: return "Windows Server 2008 R2";
            case  2: return "Windows Server 2012";
            case  3: return "Windows Server 2012 R2";
        }
    }  
    return "Windows NT (unknown)";
}

char* getWIN32_NT_10_Name(VersionInfo ver) {
   if (ver.is_workstation) {
        switch (ver.minorVersion) {
            case  0:
              /* Windows 11 21H2 (original release) build number is 22000 */
              if (ver.buildNumber >= 22000) {
                  return "Windows 11";
               } else {
                  return "Windows 10";
               }
        }
    } else {
         switch (ver.minorVersion) {
            case  0:
              /* Windows server 2019 GA 10/2018 build number is 17763 */
              /* Windows server 2022 build number is 20348 */
              if (ver.buildNumber > 20347) {
                  return "Windows Server 2022";
               } else if (ver.buildNumber > 17762) {
                  return "Windows Server 2019";
               } else {
                  return "Windows Server 2016";
               }
           }
    }
    return "Windows NT (unknown)";
  
}

char* getWIN32_NT_Name(VersionInfo ver) {
  
    if (ver.majorVersion <= 4) {
        return "Windows NT";
    }
    if (ver.majorVersion == 5) {
        return getWIN32_NT_5_Name(ver);
    }
    if (ver.majorVersion == 6) {
        return getWIN32_NT_6_Name(ver);
    }
    if (ver.majorVersion == 10) {
        return getWIN32_NT_10_Name(ver);
    }
    
    return "Windows NT (unknown)";
}

// !!!!
//#ifdef OS_WIN

char* getOsName(VersionInfo ver) {

    // WINDOWS
    if (ver.platformId == VER_PLATFORM_WIN32_WINDOWS) {
        return getWIN32_WINDOWS_Name(ver);
    }

    // NT
    if (ver.platformId == VER_PLATFORM_WIN32_NT) {
        return getWIN32_NT_Name(ver);
    }

    // UNKNOWN
    return  "Windows (unknown)";
}

char* getOsVersion(VersionInfo ver) {
   char buf[100];
   sprintf(buf, "%d.%d", ver.majorVersion, ver.minorVersion);
   return _strdup(buf);
}

char* getOsArch() {
   #if defined(_M_AMD64)
   return "amd64";
   #elif defined(_X86_)
   return "x86";
   #elif defined(_M_ARM64)
   return = "aarch64";
   #else
   return = "unknown";
   #endif
}

/*
 * User name
 * We try to avoid calling GetUserName as it turns out to
 * be surprisingly expensive on NT.  It pulls in an extra
 * 100 K of footprint.
 */
wchar_t* getUserName() {
   WCHAR *uname = _wgetenv(L"USERNAME");
   if (uname != NULL && wcslen(uname) > 0) {
      return _wcsdup(uname);
   } 
   
   DWORD buflen = 0;
   if (GetUserNameW(NULL, &buflen) == 0 && GetLastError() == ERROR_INSUFFICIENT_BUFFER) {
      uname = (WCHAR*)malloc(buflen * sizeof(WCHAR));
      if (uname != NULL && GetUserNameW(uname, &buflen) == 0) {
        free(uname);
        uname = NULL;
      }
   } else {
        uname = NULL;
   }

   if (uname != NULL) {
      return _wcsdup(uname);
   }

   return NULL;
  
}

wchar_t* getUserDir() {
    /* Current directory */
    WCHAR buf[MAX_PATH];
    if (GetCurrentDirectoryW(sizeof(buf)/sizeof(WCHAR), buf) != 0) {
      return _wcsdup(buf);
    }
    return NULL;
}


wchar_t* getUserHome() {
    /*
     * Note that we don't free the memory allocated
     * by getHomeFromShell32.
     */
    static WCHAR *u_path = NULL;
    if (u_path == NULL) {
        HRESULT hr;

        /*
         * SHELL32 DLL is delay load DLL and we can use the trick with
         * __try/__except block.
         */

        
        //__try {
        //    /*
        //     * For Windows Vista and later (or patched MS OS) we need to use
        //     * [SHGetKnownFolderPath] call to avoid MAX_PATH length limitation.
        //     * Shell32.dll (version 6.0.6000 or later)
        //     */
        //    hr = SHGetKnownFolderPath(&FOLDERID_Profile, KF_FLAG_DONT_VERIFY, NULL, &u_path);
        //} __except(EXCEPTION_EXECUTE_HANDLER) {
        //    /* Exception: no [SHGetKnownFolderPath] entry */
        //    hr = E_FAIL;
        //}
        
        hr = E_FAIL; // TODO

        if (FAILED(hr)) {
            WCHAR path[MAX_PATH+1];

            /* fallback solution for WinXP and Windows 2000 */
            hr = SHGetFolderPathW(NULL, CSIDL_FLAG_DONT_VERIFY | CSIDL_PROFILE, NULL, SHGFP_TYPE_CURRENT, path);
            if (FAILED(hr)) {
                /* we can't find the shell folder. */
                u_path = NULL;
            } else {
                /* Just to be sure about the path length until Windows Vista approach.
                 * [S_FALSE] could not be returned due to [CSIDL_FLAG_DONT_VERIFY] flag and UNICODE version.
                 */
                path[MAX_PATH] = 0;
                u_path = _wcsdup(path);
            }
        }
    }
    return u_path;
}



//#ifdef OS_WIN

////

static boolean haveMMX(void) {
    return IsProcessorFeaturePresent(PF_MMX_INSTRUCTIONS_AVAILABLE);
}

static const char* getCpuIsalist(SYSTEM_INFO& si) {
   switch (si.wProcessorArchitecture) {
    #ifdef PROCESSOR_ARCHITECTURE_IA64
    case PROCESSOR_ARCHITECTURE_IA64: return "ia64";
    #endif
    #ifdef PROCESSOR_ARCHITECTURE_AMD64
    case PROCESSOR_ARCHITECTURE_AMD64: return "amd64";
    #endif
    case PROCESSOR_ARCHITECTURE_INTEL:
        switch (si.wProcessorLevel) {
        case 6: return haveMMX()
            ? "pentium_pro+mmx pentium_pro pentium+mmx pentium i486 i386 i86"
            : "pentium_pro pentium i486 i386 i86";
        case 5: return haveMMX()
            ? "pentium+mmx pentium i486 i386 i86"
            : "pentium i486 i386 i86";
        case 4: return "i486 i386 i86";
        case 3: return "i386 i86";
        }
    }  
}

////

static char* getEncodingInternal(LCID lcid) {
    int codepage = 0;
    char* ret = (char*) malloc(16);
    if (ret == NULL) {
        return NULL;
    }

    if (lcid == 0) {
        codepage = GetACP();
        _itoa_s(codepage, ret + 2, 14, 10);
    } else if (GetLocaleInfo(lcid, LOCALE_IDEFAULTANSICODEPAGE, ret + 2, 14) != 0) {
        codepage = atoi(ret + 2);
    }

    switch (codepage) {
    case 0:
    case 65001:
        strcpy(ret, "UTF-8");
        break;
    case 874:     /*  9:Thai     */
    case 932:     /* 10:Japanese */
    case 949:     /* 12:Korean Extended Wansung */
    case 950:     /* 13:Chinese (Taiwan, Hongkong, Macau) */
    case 1361:    /* 15:Korean Johab */
        ret[0] = 'M';
        ret[1] = 'S';
        break;
    case 936:
        strcpy(ret, "GBK");
        break;
    case 54936:
        strcpy(ret, "GB18030");
        break;
    default:
        ret[0] = 'C';
        ret[1] = 'p';
        break;
    }
 
    return ret;
}

////

static Locale* loadLocale(LCID lcid) {

    /* script */
    char tmp[SNAMESIZE];
    char* script = (char*) malloc(PROPSIZE);
    if (script == NULL) {
        return NULL;
    }

    #ifdef LOCALE_SNAME
    if (GetLocaleInfo(lcid,
                      LOCALE_SNAME, tmp, SNAMESIZE) == 0 ||
        sscanf(tmp, "%*[a-z\\-]%1[A-Z]%[a-z]", script, &((script)[1])) == 0 ||
        strlen(script) != 4) {
        script[0] = '\0';
    }
    #else
    script[0] = '\0';
    #endif

    /* country */
    char* country = (char*) malloc(PROPSIZE);
    if (country == NULL) {
        return NULL;
    }
    if (GetLocaleInfo(lcid, LOCALE_SISO3166CTRYNAME, country, PROPSIZE) == 0) {
        #ifdef LOCALE_SNAME
        if (GetLocaleInfo(lcid, LOCALE_SISO3166CTRYNAME2, country, PROPSIZE) == 0) {
          country[0] = '\0';
        }
        #else
        country[0] = '\0';
        #endif                
    }

    /* language */
    char* language = (char*) malloc(PROPSIZE);
    if (language == NULL) {
        return NULL;
    }
    if (GetLocaleInfo(lcid, LOCALE_SISO639LANGNAME, language, PROPSIZE) == 0) {

        #ifdef LOCALE_SISO639LANGNAME2
        if (GetLocaleInfo(lcid, LOCALE_SISO639LANGNAME2, language, PROPSIZE) == 0) {
            /* defaults to en_US */
            strcpy(language, "en");
            strcpy(country, "US");
        }
        #else
        /* defaults to en_US */
        strcpy(language, "en");
        strcpy(country, "US");
        #endif
    }

    /* variant */
    char* variant = (char*) malloc(PROPSIZE);
    if (variant == NULL) {
        return NULL;
    }
    (variant)[0] = '\0';

    /* handling for Norwegian */
    if (strcmp(language, "nb") == 0) {
        strcpy(language, "no");
        strcpy(country , "NO");
    } else if (strcmp(language, "nn") == 0) {
        strcpy(language, "no");
        strcpy(country , "NO");
        strcpy(variant, "NY");
    }

    /* encoding */
    char* encoding = getEncodingInternal(lcid);

    Locale* locale = new Locale();
    locale->language = language;
    locale->script = script;
    locale->country = country;
    locale->variant = variant;
    locale->encoding = encoding;
 
    return locale;
}

////

void initLocaleWin(SysInfo& sysInfo) {
  /*
   * query the system for the current system default locale
   * (which is a Windows LCID value),
   */
   LCID userDefaultLCID = GetUserDefaultLCID();
   LANGID userDefaultUILang = GetUserDefaultUILanguage();
   LCID userDefaultUILCID = MAKELCID(userDefaultUILang, SORTIDFROMLCID(userDefaultLCID));

   char * display_encoding;
   HANDLE hStdOutErr;

    // Windows UI Language selection list only cares "language"
    // information of the UI Language. For example, the list
    // just lists "English" but it actually means "en_US", and
    // the user cannot select "en_GB" (if exists) in the list.
    // So, this hack is to use the user LCID region information
    // for the UI Language, if the "language" portion of those
    // two locales are the same.
    if (PRIMARYLANGID(LANGIDFROMLCID(userDefaultLCID)) == PRIMARYLANGID(userDefaultUILang)) {
      userDefaultUILCID = userDefaultLCID;
    }

    Locale* formatLocale = loadLocale(userDefaultLCID);    // LC_CTYPE
    Locale* displayLocale = loadLocale(userDefaultUILCID); // LC_MESSAGES

    // TODO: Use initLocale(sysInfo, cat, locale) for LC_CTYPE, LC_MESSAGES

    if (formatLocale != nullptr) {
       if (formatLocale->language != nullptr) {
        sysInfo.format_language = formatLocale->language;
      }
      if (formatLocale->script != nullptr) {
        sysInfo.format_script = formatLocale->script;
      }
      if (formatLocale->country != nullptr) {
        sysInfo.format_country = formatLocale->country;
      }
      if (formatLocale->variant != nullptr) {
        sysInfo.format_variant = formatLocale->variant;
      }
      if (formatLocale->encoding != nullptr) {
        sysInfo.encoding = formatLocale->encoding;
      }
    }

    if (displayLocale != nullptr) {
       if (displayLocale->language != nullptr) {
        sysInfo.display_language = displayLocale->language;
      }
      if (displayLocale->script != nullptr) {
        sysInfo.display_script = displayLocale->script;
      }
      if (displayLocale->country != nullptr) {
        sysInfo.display_country = displayLocale->country;
      }
      if (displayLocale->variant != nullptr) {
        sysInfo.display_variant = displayLocale->variant;
      }
      //if (displayLocale->encoding != nullptr) {
      //  sysInfo.encoding = displayLocale->encoding;
      //}
    }

}

void initSysInfoWin(SysInfo& sysInfo) {

  int majorVersion = 0;
  int minorVersion = 0;
  int buildNumber = 0;

  /* tmp dir */
  WCHAR tmpdir[MAX_PATH + 1];

  GetTempPathW(MAX_PATH + 1, tmpdir);
  sysInfo.tmp_dir = _wcsdup(tmpdir);

  /* OS properties */
  char buf[100];
  boolean is_workstation;
  boolean is_64bit;
  DWORD platformId;

  ////
  OSVERSIONINFOEX ver;
  ver.dwOSVersionInfoSize = sizeof(ver);

  GetVersionEx((OSVERSIONINFO *) &ver);
  majorVersion = ver.dwMajorVersion;
  minorVersion = ver.dwMinorVersion;

   /* Distinguish Windows Server 2016+ by build number */
   buildNumber = ver.dwBuildNumber;
   is_workstation = (ver.wProductType == VER_NT_WORKSTATION);
   platformId = ver.dwPlatformId;

   //sysInfo.patch_level = _strdup(ver.szCSDVersion);    

   ////

   SYSTEM_INFO si;
   ZeroMemory(&si, sizeof(SYSTEM_INFO));
   GetNativeSystemInfo(&si);

   is_64bit = (si.wProcessorArchitecture == PROCESSOR_ARCHITECTURE_AMD64);

   // TODO: Load from kernel32.DLL

   VersionInfo versionInfo;
   
   versionInfo.platformId = platformId;
   versionInfo.majorVersion = majorVersion;
   versionInfo.minorVersion = minorVersion;

   versionInfo.is_workstation = is_workstation;
   versionInfo.is_64bit = is_64bit;

   /* OS */
   sysInfo.os_name = getOsName(versionInfo);
   sysInfo.os_version = getOsVersion(versionInfo);
   sysInfo.os_arch = getOsArch();

   /* CPU */
   //sysInfo.os_arch = cpu_isalist;
   sysInfo.cpu_isalist = getCpuIsalist(si);

   /* User */
   sysInfo.user_name = getUserName();
   sysInfo.user_dir = getUserDir();
   sysInfo.user_home = getUserHome();
   if (sysInfo.user_home == NULL) {
    sysInfo.user_home = L"C:\\";
   }

 
}
#endif


//// UNIX ////

#ifdef OS_UNIX

void initLocaleUnix(SysInfo& sysInfo) {
  #ifdef OS_MAC
  initLocaleMac(sysInfo);
  #else
  initLocalePosix(sysInfo);
  #endif
}

void initSysInfoUnix(SysInfo& sysInfo) {

   /* Endianness of platform */
   unsigned int endianTest = 0xff000000;
   if (((char*) (&endianTest))[0] != 0) {
      sysInfo.cpu_endian = "big";
   } else {
      sysInfo.cpu_endian = "little";
   }

   struct utsname name;
   uname(&name);

   /* OS */
   #ifdef OS_MAC
     initOsMac(sysInfo);
     //sysInfo.os_arch = strdup(name.machine); 
   #else

    //struct utsname name;
    //uname(&name);
    sysInfo.os_name = strdup(name.sysname);

    #ifdef _AIX
        char os_version[strlen(name.version) + strlen(name.release) + 2];
        strcpy(os_version, name.version);
        strcat(os_version, ".");
        strcat(os_version, name.release);
        sysInfo.os_version = os_version;
    #else
        sysInfo.os_version = strdup(name.release);
    #endif

   #endif
   sysInfo.os_arch = strdup(name.machine); 

  /* User */
  struct passwd *pwent = getpwuid(getuid());
  if (pwent) {
    sysInfo.user_name = strdup(pwent->pw_name);
    sysInfo.user_home = strdup(pwent->pw_dir);
  }

   /* Current directory */
   //int PATH_MAX_ = 1024;
   char buf[PATH_MAX];
   errno = 0;
   if (getcwd(buf, sizeof(buf)) == NULL) {
       //error("System Properties init: Can't get current working directory.");
       std::cerr << "System Properties init: Can't get current working directory." << std::endl;
   } else {
       sysInfo.user_dir = strdup(buf);
   }
   //#endif

   #ifdef OS_MAC
    /* Darwin has a per-user temp dir */
    static char tmp_path[PATH_MAX]; // static - important
    int pathSize = confstr(_CS_DARWIN_USER_TEMP_DIR, tmp_path, PATH_MAX);
    if (pathSize > 0 && pathSize <= PATH_MAX) {
        sysInfo.tmp_dir = tmp_path;
    }
   #else 
     sysInfo.tmp_dir = P_tmpdir;
   #endif

   sysInfo.file_separator = "/";
   sysInfo.line_separator = "\n";

}
#endif // OS_UNIX

void initLocale(SysInfo& sysInfo) {
  #ifdef OS_WIN
  initLocaleWin(sysInfo);
  #else
  initLocaleUnix(sysInfo);
  #endif
}

void initSysInfo(SysInfo& sysInfo) {
  #ifdef OS_WIN
  initSysInfoWin(sysInfo);
  #else
  initSysInfoUnix(sysInfo);
  #endif
}
}


#include "sysinit.h"

#ifdef OS_WIN
#include <io.h>
#include <windows.h>
#else
#include <unistd.h>
#include <dlfcn.h>

#include <sys/utsname.h>        /* For os_name and os_version */
//#include <langinfo.h>         /* For nl_langinfo */
//#include <locale.h>
#include <pwd.h>
#endif

#ifdef OS_MAC
#include <CoreFoundation/CoreFoundation.h>
#include <CoreServices/CoreServices.h>
#endif

#include "plazma/kernel/lib/str/strlib.h"

namespace syslib {

void setLocale(SysInfo& sysInfo, char* lc) {
  if (lc == nullptr) {
    return;
  }
  sysInfo.locale = strdup(lc);

  Locale* locale = parseLocale(sysInfo.locale);
  if (locale != nullptr) {
    
    sysInfo.format_language = locale->language;
    sysInfo.format_country = locale->country;
    sysInfo.encoding = locale->encoding;

    delete locale;
  }

}

// "en_US.UTF-8"

void initDefaultLocale(SysInfo& sysInfo) {
  sysInfo.locale = "en_US.UTF-8";
  sysInfo.format_language = "en";
  sysInfo.format_country = "US";
  sysInfo.encoding = "UTF-8";

  //sysInfo.locale = "UTF-8";
  //sysInfo.locale = "en_US";
  //sysInfo.locale = "en_US.";

  //setLocale(sysInfo, sysInfo.locale);
}

#ifdef OS_MAC

// FRAMEWORK
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

       std::string osName = "";
       std::string osVersion = "";
       //std::string osBuild = "";

       std::string line = "";

       for (int i = 0; i < size; i++) {
         line = lines[i];
         if (strlib::startsWith(line, PRODUCT_NAME)) {
           osName = line.substr(PRODUCT_NAME.length());
           osName = strlib::trimAll(osName);
           sysInfo.os_name = strdup(osName.c_str());
         } else if (strlib::startsWith(line, PRODUCT_VERSION)) {
           osVersion = line.substr(PRODUCT_VERSION.length());
           osVersion = strlib::trimAll(osVersion);
           sysInfo.os_version = strdup(osVersion.c_str());
         }

         // else if (strlib::startsWith(line, BUILD_VERSION)) {
         //  osBuild = line.substr(BUILD_VERSION.length());
         //  osBuild = strlib::trimAll(osBuild);
         //}
       }

       //ProductName    :	Mac OS X
       //ProductVersion :	10.14.6
       //BuildVersion   :	18G95
}

void initOsMac(SysInfo& sysInfo) {
  initOsMac_F(sysInfo);
}

#endif

#ifdef OS_WIN
void initSysInfoWin(SysInfo& sysInfo) {
  // TODO
}
#endif

#ifdef OS_UNIX
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
     sysInfo.os_arch = strdup(name.machine); 
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
       //std::cerr << "System Properties init: Can't get current working directory." << std::endl;
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
     // TODO: /var/tmp or /tmp
   #endif


   sysInfo.file_separator = "/";
   sysInfo.line_separator = "\n";

}
#endif

/*
static int ParseLocale(int cat, char ** std_language, char ** std_script,
                       char ** std_country, char ** std_variant, char ** std_encoding) {
    char *temp = NULL;
    char *language = NULL, *country = NULL, *variant = NULL,  *encoding = NULL;
    char *p, *encoding_variant, *old_temp, *old_ev;
    char *lc;

    lc = setlocale(cat, NULL);
}
*/

#ifdef OS_MAC

const char* getLocaleValue(CFLocaleRef locale, CFLocaleKey key) {
  CFStringRef value = (CFStringRef) CFLocaleGetValue(locale, key); 
  const char* ch = CFStringGetCStringPtr(value, kCFStringEncodingUTF8);
  if (ch == nullptr) {
    return nullptr;
  }
  return ch;
}

// FRAMEWORK
void initLocaleMac_F(SysInfo& sysInfo) {

  CFLocaleRef cflocale = CFLocaleCopyCurrent();

  const char* locale = getLocaleValue(cflocale, kCFLocaleIdentifier);

  const char* language = getLocaleValue(cflocale, kCFLocaleLanguageCode);
  const char* country = getLocaleValue(cflocale, kCFLocaleCountryCode);
  const char* script = getLocaleValue(cflocale, kCFLocaleScriptCode);
  const char* variant = getLocaleValue(cflocale, kCFLocaleVariantCode);
  const char* encoding = nullptr; //getLocaleValue(cflocale, kCFLocaleExemplarCharacterSet);

  //CFStringRef identifier = CFLocaleGetIdentifier(cflocale);
  //const char* ch = CFStringGetCStringPtr(identifier, kCFStringEncodingUTF8);

  CFRelease(cflocale);

  if (locale) {
    sysInfo.locale = strdup(locale);
  } else {

    char* lc = getLocale(); 
    setLocale(sysInfo, lc);
    return;

  }

  if (language) {
    sysInfo.format_language = strdup(language);
  }
  if (country) {
    sysInfo.format_country = strdup(country);
  }
  if (script) {
    sysInfo.format_script = strdup(script);
  }
  if (variant) {
    sysInfo.format_variant = strdup(variant);
  }

  if (encoding) {
    sysInfo.encoding = strdup(encoding);
  } else {

    char* lc = getLocale(); 

    // Empty
    if (isEmptyLocale(lc)) {
      lc = "en_US.UTF-8"; // TODO
      //initDefaultLocale(sysInfo);
      //return;
    }

    Locale* ulocale = parseLocale(lc);
    if (!ulocale || !ulocale->encoding) {
      return;
    }
    sysInfo.encoding = strdup(ulocale->encoding);
    
  }
  

}

////===


// ALTERNATIVE
void initLocaleMac_A(SysInfo& sysInfo) {

  char* lc = nullptr;

  // Test locale
  lc = getLocale(LC_CTYPE);

  if (isEmptyLocale(lc)) {
    setDefaultLocale();
  }

  int cat = LC_CTYPE;
  //int cat = LC_MESSAGES;
  //int cat = LC_ALL;
  lc = getLocale(cat);

  // Empty
  if (isEmptyLocale(lc)) {
    initDefaultLocale(sysInfo);
    return;
  }

  // UTF-8
  //if (isLocale(lc, "UTF-8")) {
  //  initDefaultLocale(sysInfo);
  //  return;
  //}

  setLocale(sysInfo, lc);

}

void initLocaleMac(SysInfo& sysInfo) {
  initLocaleMac_F(sysInfo);
  //initLocaleMac_A(sysInfo);
}

#endif


void initLocale(SysInfo& sysInfo) {

  /*
  setlocale(LC_ALL, "");
  int cat = LC_CTYPE;
  //int cat = LC_MESSAGES;
  //int cat = LC_ALL;
  char *lc = setlocale(cat, "");
  if (lc == NULL) {
    return;
  }
  //sysInfo.format_country = strdup(lc);
  */

  #ifdef OS_MAC
  initLocaleMac(sysInfo);
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

#ifndef PLAZMA_LIB_SYSINFO_H
#define PLAZMA_LIB_SYSINFO_H

#ifdef OS_WIN
#include <windows.h>
typedef wchar_t nchar;
#else
typedef char nchar;
#endif

#include "syslocale.h"

namespace syslib {

  typedef struct {

    char* os_name;
    char* os_version;
    char* os_release; // *
    char* os_arch;
    char* os_arch_data;

    nchar* user_name;
    nchar* user_home;
    nchar* user_dir;
    nchar* tmp_dir;

    char* file_separator;
    char* path_separator; // ?
    char* line_separator;

    char* format_locale;
    char* format_language;
    char* format_script;
    char* format_country;
    char* format_variant;

    char* display_locale;
    char* display_language;    
    char* display_script;    
    char* display_country;    
    char* display_variant;
    char* encoding; // file_encoding

    char* stdout_encoding;
    char* stderr_encoding;

    char* unicode_encoding;     // The default endianness of unicode i.e. UnicodeBig or UnicodeLittle
    const char* cpu_isalist;    // list of supported instruction sets
    char* cpu_endian;           // endianness of platform

    bool init = false;

  } SysInfo;

  void initLocale(SysInfo& sysInfo, int cat, Locale* locale);

  void initLocale(SysInfo& sysInfo, int cat, char* name);

  //void initLocale(SysInfo& sysInfo, char* name); // ?

  void initDefaultLocale(SysInfo& sysInfo);

  void initLocalePosix(SysInfo& sysInfo);

}

#endif // PLAZMA_LIB_SYSINFO_H
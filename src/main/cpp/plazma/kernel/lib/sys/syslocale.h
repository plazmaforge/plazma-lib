#ifndef PLAZMA_KERNEL_LIB_SYSLOCALE_H
#define PLAZMA_KERNEL_LIB_SYSLOCALE_H

//#include <string>
#include <locale>

namespace syslib {

typedef struct {

    char* name;

    char* language;
    char* script;
    char* country;
    char* variant;
    char* encoding;

} Locale;

  void setDefaultLocale();

  char* getLocale(int cat);

  char* getLocale();

  bool isEmptyLocale(char* locale);

  bool equalsLocale(char* locale1, char* locale2);

  Locale* parseLocale(char* locale);

  Locale* loadLocale(int cat);

}

#endif // PLAZMA_KERNEL_LIB_SYSLOCALE_H
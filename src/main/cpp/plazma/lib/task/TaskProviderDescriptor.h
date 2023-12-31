#ifndef PLAZMA_LIB_TASK_TASK_PROVIDER_DESCRIPTOR_H
#define PLAZMA_LIB_TASK_TASK_PROVIDER_DESCRIPTOR_H

#include <string>
#include <vector>

#include "plazma/lib/sys/LibraryLoader.h"
#include "TaskProvider.h"

//using namespace sys;

namespace task {

    class TaskProviderDescriptor {

        public:

          TaskProvider* provider;
          std::string providerName;
          std::string packageName;
          std::string libraryName;
          std::string libraryPath; // depends on OS
          sys::LibraryLoader<TaskProvider>* loader;
          bool initialized;
          bool hasError;
          bool hasLibrary;

        public:

            TaskProviderDescriptor();

            ~TaskProviderDescriptor();

            void destroy();

    };

}
#endif // PLAZMA_LIB_TASK_TASK_PROVIDER_DESCRIPTOR_H
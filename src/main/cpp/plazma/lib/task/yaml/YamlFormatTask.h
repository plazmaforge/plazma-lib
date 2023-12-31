#ifndef PLAZMA_LIB_TASK_YAML_YAML_FORMAT_TASK_H
#define PLAZMA_LIB_TASK_YAML_YAML_FORMAT_TASK_H

#include "plazma/lib/task/format/FormatTask.h"

const std::string TASK_FORMAT_YAML = "format-yaml";

namespace task {

    class YamlFormatTask: public FormatTask {

        public:

            ///////////////////////////////////////////////////////////
            // errors:
            ///////////////////////////////////////////////////////////

            const std::string ERROR_YAML_NODE_EMPTY = "Can't execute task: YAML Node is empty";
            const std::string ERROR_YAML_TOKENS_EMPTY = "Can't execute task: YAML Tokens are empty";

            YamlFormatTask();

            ~YamlFormatTask();

            virtual void execute(TaskContext* ctx);

            virtual void initParameters();

    };

}
#endif // PLAZMA_LIB_TASK_YAML_YAML_FORMAT_TASK_H
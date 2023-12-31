#ifndef PLAZMA_LIB_DATA_JSON_JSON_PARSER_CONTEXT_H
#define PLAZMA_LIB_DATA_JSON_JSON_PARSER_CONTEXT_H

#include <string>
#include <map>

#include "plazma/lib/data/node/Node.h"
#include "plazma/lib/text/ParserContext.h"

using namespace text;

namespace json {

    class JsonParserContext: public ParserContext {

        public:
            JsonParserContext();
            ~JsonParserContext();

            std::string toString();

        public:
            int currEvent = 0;
            int prevEvent = 0;
            int nodeEvent = 0;

            char* currAttribute = nullptr;

            node::Node* currNode = nullptr;
            std::map<int, char*> map;
            bool isEmptyContainer = false;
    };

}
#endif // PLAZMA_LIB_DATA_JSON_JSON_PARSER_CONTEXT_H
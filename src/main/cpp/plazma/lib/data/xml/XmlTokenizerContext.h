#ifndef PLAZMA_LIB_DATA_XML_XML_TOKENIZER_CONTEXT_H
#define PLAZMA_LIB_DATA_XML_XML_TOKENIZER_CONTEXT_H

#include <string>

#include "plazma/lib/text/TokenizerContext.h"

using namespace text;

namespace xml {

    class XmlTokenizerContext: public TokenizerContext {

        public:
        
            XmlTokenizerContext();

            ~XmlTokenizerContext();

            void updateState(std::string separator);

            bool isQuoteChar(char ch);

            bool isSeparatorChar(char ch);

            std::string toString();

    };

}
#endif // PLAZMA_LIB_DATA_XML_XML_TOKENIZER_CONTEXT_H
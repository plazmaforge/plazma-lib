#ifndef PLAZMA_LIB_DATA_XML_XML_STRING_APPENDABLE_H
#define PLAZMA_LIB_DATA_XML_XML_STRING_APPENDABLE_H

#include <string>
#include "XmlAppendable.h"

namespace xml {

    class XmlStringAppendable : public XmlAppendable {

        public:

          XmlStringAppendable();

          ~XmlStringAppendable();

          ////

          void setColorized(bool colorized);

          void append(const std::string &str);

          void appendTag(const std::string &str);

          void appendTagName(const std::string &str);

          void appendAttributeName(const std::string &str);

          void appendAttributeValue(const std::string &str);

          void appendText(const std::string &str);

          void appendCDATA(const std::string &str);

          ////

          void appendWrap(const std::string &str, int color);

          std::string toString();

        public:

          bool colorized = false;

        private:

          std::string buf;

    };

}
#endif // PLAZMA_LIB_DATA_XML_XML_STRING_APPENDABLE_H
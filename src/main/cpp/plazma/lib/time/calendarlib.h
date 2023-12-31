#ifndef PLAZMA_LIB_TIME_CALENDARLIB_H
#define PLAZMA_LIB_TIME_CALENDARLIB_H

#include <string>
#include <vector>

//#include "datelib.h"

namespace calendarlib {

    std::vector<std::string> toMonthCalendarLines(int year, int month, bool sundayFirst, bool upper);

    std::vector<std::string> toYearCalendarLines(int year, bool sundayFirst, bool upper);

    ////

    void printMonthCalendar(int year, int month);

    void printMonthCalendar(int year, int month, bool sundayFirst);

    void printMonthCalendar(int year, int month, bool sundayFirst, bool upper);

    void printYearCalendar(int year, bool sundayFirst);

    void printYearCalendar(int year, bool sundayFirst, bool upper);

}

#endif // PLAZMA_LIB_TIME_CALENDARLIB_H
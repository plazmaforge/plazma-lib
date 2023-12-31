#include "test.h"

char* strnew(const int len) {
    if (len < 0) {
        return NULL;
    }
    char* res = (char*) malloc(len + 1);
    if (res == NULL) {
        return NULL;
    }
    for (int i = 0; i < len + 1; i++)
        res[i] = '\0';
    return res;
}

// strdup, strcpynew
char* strnew(const char* str) {
    if (str == NULL) {
        return NULL;
    }
    char* res = strnew(strlen(str));
    if (res == NULL) {
        return NULL;
    }
    strcpy(res, str);
    return res;
}

char* strcatnew(const char* str1, const char* str2) {
    if (str1 == NULL || str2 == NULL) {
        return NULL;
    }
    char* res = strnew(strlen(str1) + strlen(str2));
    if (res == NULL) {
        return NULL;
    }
    strcpy(res, str1);
    strcat(res, str2);
    return res;
}

TestCase* findTestCaseByFile(const char* file) {
    if (testCases.empty()) {
        return NULL;
    }
    TestCase* testCase = NULL;
    for (int i = 0; i < testCases.size(); i++) {
        testCase = testCases[i];
        if (strcmp(testCase->file, file) == 0) {
            return testCase;
        }
    }
    return NULL;
}

TestCase* findTestCaseByName(const char* name) {
    if (testCases.empty()) {
        fprintf(stderr, "[ERROR] No registered TestCases\n"); 
        return NULL;
    }
    TestCase* testCase = NULL;
    for (int i = 0; i < testCases.size(); i++) {
        testCase = testCases[i];
        if (strcmp(testCase->name, name) == 0) {
            return testCase;
        }
    }
    return NULL;
}

Test* findTestByName(TestCase* testCase, const char* name) {
    if (testCase == NULL) {
        return NULL;
    }
    Test* test = NULL;
    for (int i = 0; i < testCase->tests.size(); i++) {
        test = testCase->tests[i];
        if (strcmp(test->name, name) == 0) {
            return test;
        }
    }
    return NULL;
}

void registerTestCase(const char* file, const char* name, void (*setall)()) {
    TestCase* testCase = new TestCase();
    if (file) {
        testCase->file = strnew(file);
    }
    if (name) {
        testCase->name = strnew(name);
    }
    testCase->setall = setall;
    testCases.push_back(testCase);
}

void registerTest(const char* file, const char* name, void (*func)()) {
    TestCase* testCase = findTestCaseByFile(file);
    if (testCase == NULL) {
        return;
    }
    Test* test = new Test();
    test->parent = testCase;
    if (name) {
        test->name = strnew(name);
    }
    test->func = func;
    testCase->tests.push_back(test);
}

void runTest(Test* test) {
    if (test == NULL) {
        return;
    }
    if (test->func == NULL) {
        return;
    }

    test->started = true;
    test->parent->started++;
    
    test->func();
}

void fill(char* array, int len, char value) {
    if (len == 0) {
        return;
    }    
    for (int i = 0; i < len - 1; i++) {
        array[i] = value;
    }
    array[len - 1] = '\0';
}

void fill(char* array, int len) {
    fill(array, len, ' ');
}

int getPadLen(int len) {
    int MAX_LEN = 80;
    return (len < MAX_LEN) ? (MAX_LEN - len) : 0;
}

void printTotalResult() {
    if (testCases.empty()) {
        fprintf(stdout, "No Tests\n"); 
        return;
    }
    TestCase* testCase = NULL;
    int total = 0;
    int started = 0;
    int failed = 0;
    int passed = 0;
    for (int i = 0; i < testCases.size(); i++) {
        testCase = testCases[i];
        total += testCase->tests.size();
        started += testCase->started;
        failed += testCase->failed;
    }
    passed = started - failed;

    fprintf(stdout, "\n");

    if (started == 0) {
        fprintf(stdout, "No started Tests\n"); 
        return;
    } 

    if (failed > 0) {
        //fprintf(stdout, "%d TEST FAILED\n", failed); 
        fprintf(stdout, "TEST FAILED: %d\n", failed); 
    }
    fprintf(stdout, "TEST PASSED: %d\n", passed);
    fprintf(stdout, "TEST TOTAL : %d\n", started);
    fprintf(stdout, "\n");
    fprintf(stdout, (failed > 0 ? "FAILED" : "OK"));
    fprintf(stdout, "\n");
}

void printTestResult(const char* file, const char* name, Test* test) {
    int padLen = getPadLen(strlen(file) + strlen(name) + strlen(test->name) + 4); // +18 = 7 + 4 + 1 + 6
    char pad[padLen];
    fill(pad, padLen);

    fprintf(stdout, "[TEST] %s: %s: %s %s" , file, name, test->name, pad);
    fprintf(stdout, (test->failed ? "- FAIL\n" : "- OK\n"));
}

void printTestCaseResult(const char* file, const char* name, TestCase* testCase, bool isPrintTest) {
    int padLen = getPadLen(strlen(file) + strlen(name) + 2);
    char pad[padLen];
    fill(pad, padLen);

    fprintf(stdout, (isPrintTest ? "[CASE] %s: %s %s" : "[TEST] %s: %s %s"), file, name, pad);
    fprintf(stdout, (testCase->failed > 0 ? "- FAIL\n" : "- OK\n"));

    //if (testCase->failed > 0) {
        //fprintf(stdout, "[FAILED ] '%s: %s'\n", file, name); 
    //} else {
        //fprintf(stdout, "[PASSED ] '%s: %s'\n", file, name); 
    //}
}

void runTestCase(TestCase* testCase) {

    std::vector<Test*> tests = testCase->tests;
    if (tests.empty()) {
        return;
    }

    //fprintf(stdout, "[RUNNNING] %s: %s\n", file, name);
    //fprintf(stdout, "[RUNNNING] %s: %s\t", file, name);

    int printMode = 3; // 1 - Test, 2 - TestCase, 3 - Test & TestCase
    bool isPrintTest = printMode == 1 || printMode == 3;
    bool isPrintCase = printMode == 2 || printMode == 3;;

    //testCase->started = true;

    Test* test = NULL;
    for (int i = 0; i < tests.size(); i++) {
        test = tests[i];
        runTest(test);
                
        if (isPrintTest) {
            printTestResult(testCase->file, testCase->name, test);
        }
    }

    if (isPrintCase) {
        printTestCaseResult(testCase->file, testCase->name, testCase, isPrintTest);
    }

}

void runTestCase(const char* file, const char* name) {
    TestCase* testCase = findTestCaseByName(name);
    if (testCase == NULL) {
        fprintf(stderr, "[ERROR] TestCase not found: %s: %s\n", file, name); 
        return;
    }

    runTestCase(testCase);    
}

void runAll() {
    if (testCases.empty()) {
        fprintf(stderr, "[ERROR] No registered TestCases\n"); 
        return;
    }
    TestCase* testCase = NULL;
    for (int i = 0; i < testCases.size(); i++) {
        testCase = testCases[i];
        runTestCase(testCase);
    }
}

void registerError(const char* file, const int line, const char* func) {
    TestCase* testCase = findTestCaseByFile(file);
    if (testCase) {
        //testCase->failed++;
        Test* test = findTestByName(testCase, func);
        if (test) {
            test->asserted++;
            testCase->asserted++;
            if (test->failed) {
                return;
            }
            test->failed = true;
            testCase->failed++;
        }
    }
}

void fail(const char* file, const int line, const char* func, const char* message) {
    fprintf(stderr, "[FAIL] Assertion failed in %s on line %d: %s\n", file, line, message); 
    registerError(file, line, func);
}

// op
void fail(const char* file, const int line, const char* func, const char* a, const char* op, const char* b) {
    fprintf(stderr, "[FAIL] Assertion failed in %s on line %d: %s %s %s\n", file, line, a, op, b); 
    registerError(file, line, func);
}

// op
void fail(const char* file, const int line, const char* func, const std::string& a, const char* op, const std::string& b) {
    fprintf(stderr, "[FAIL] Assertion failed in %s on line %d: %s %s %s\n", file, line, a.c_str(), op, b.c_str()); 
    registerError(file, line, func);
}

////

std::string toString(const std::string& value) {
    return "\"" + value + "\"";
}

std::string toString(const std::vector<std::string>& values) {
    if (values.empty()) {
        return "[]";
    }
    std::string result = "[";
    for (int i = 0; i < values.size(); i++) {
        if (i > 0) {
            result.append(", ");
        }
        result.append(values[i]);
    }
    result += "]";
    return result;
}

std::string toString(const short value) {
    return std::to_string(value);
}

std::string toString(const int value) {
    return std::to_string(value);
} 

std::string toString(const long value) {
    return std::to_string(value);
}

std::string toString(const float value) {
    return std::to_string(value);
}

std::string toString(const double value) {
    return std::to_string(value);
}
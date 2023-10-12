#include <gtest/gtest.h>
using namespace testing;


extern "C"
{
#include "magical_number.h"
}

TEST(magical_number, test_magical_number)
{
    /* test magical_number function returns 7 */
    EXPECT_EQ(7, magical_number());
}
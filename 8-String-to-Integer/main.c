int myAtoi(char* s) {
    int i = 0;
    int sign = 1;
    long result = 0;

    while (s[i] == ' ') {
        i++;
    }

    if (s[i] == "-" || s[i] == "+") {
        if (s[i] == "-") {
            sign = -1;
        }
        i++;
    }

    while (s[i] >= '0' && s[i] <= '9'){
        result = result * 10 + (s[i] - '0');
        i++;
        if (result*sign > 2147483647) {
            return 2147483647;
        }
        if (result*sign < -2147483648) {
            return -2147483648;
        }
    }
    return (int)(result * sign);
}
#include <iostream>

template <typename T, size_t N>
void printArray(T (&arr)[N]) {
    for (size_t i = 0; i < N; ++i) {
        std::cout << arr[i] << ' ';
    }
    std::cout << '\n';
}

int main() {
    int intArr[] = {1, 2, 3, 4, 5};
    printArray(intArr);

    double doubleArr[] = {1.1, 2.2, 3.3, 4.4, 5.5};
    printArray(doubleArr);

    return 0;
}
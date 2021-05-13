#include <iostream>
int main() {
	for (int i = 0; i < 100; i++) {
		if ((1 << i) % i == 2 % i) {
			std::cout << i << " ";
		}
	}
}

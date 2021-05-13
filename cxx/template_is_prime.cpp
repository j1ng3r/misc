#include <iostream>
#include <type_traits>

template <int a, int b>
constexpr bool greaterthan = a > b;

template <int base, int exp, typename = std::enable_if<exp == 0>>
constexpr int pow_ = 1;

template <int base, int exp, typename = std::enable_if<greaterthan<exp, 0>>>
constexpr int pow_ = base * pow<base, exp - 1>

template <int x, int i, typename = std::enable_if<greaterthan<i*i, x>>>
constexpr bool is_prime_rec = true;



template <int x, int i, typename, typename = std::enable_if<x % i != 0>>
constexpr bool is_prime_rec = false;

template <int x, int i>
constexpr bool is_prime_rec = i*i > x || (x % i != 0 && is_prime_rec<x, i + 1>);

template <int x>
constexpr bool is_prime = is_prime_rec<x, 2>;

int main() noexcept {
   std::cout << is_prime<2>;
	std::cout << is_prime<3>;
	std::cout << is_prime<4>;
	std::cout << is_prime<5>;
	std::cout << is_prime<6>;
	std::cout << is_prime<7>;
	std::cout << is_prime<8>;
	std::cout << is_prime<9>;
	std::cout << is_prime<10>;
}

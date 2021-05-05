#include <vector>
#include <iostream>

using u8 = unsigned char;

struct Interpreter {
	u8 arr[4]{255, 255, 255, 255};
	u8 fac{48};
	u8 order;
	u8 parity;
	u8 len;
};

void sendCard(Interpreter* self, u8 card) {
	self->parity ^= card & 1;
	self->len++;
	self->fac /= self->len;
	u8 i = 0;
	while(self->arr[i] < card) i++;
	self->order += self->fac * i;
	while(i < self->len) {
		u8 temp = self->arr[i];
		self->arr[i] = card;
		card = temp;
		i++;
	}
	self->arr[i] = card; // This will auto-sort arr as it gets built
	// Uses insertion sort
	// Perhaps arr should actually be a priority queue
}

u8 calculateHiddenCard(Interpreter* self) {
	u8 hiddenCard = self->order + self->parity;
	for(u8 i = 0; i < 4; i++) if(hiddenCard >= self->arr[i]) hiddenCard++;
	return hiddenCard;
}

bool cardsAreSorted(u8* cards) {
	u8 max = 255;
	for(int i = 4; i >= 0; i--) {
		if(max < cards[i]) {
			return false;
		}
		max = cards[i];
	}
	return true;
}

bool sendCards(u8* cards) {
	u8 parity = 0;
	for(int i = 0; i < 4; i++) {
		parity ^= cards[i] & 1;
	}
	u8 hidden = cards[parity];
	u8 order = (hidden - parity) / 2;
	parity ^= 1;
	std::vector<u8> all_indices{parity, 2, 3, 4};
	u8 divisors[4]{1, 4, 12, 24};
	u8 indices[4]{};
	for(int i = 0; i < 4; i++) {
		u8 index = order / divisors[i] % (4 - i);
		indices[i] = all_indices[index];
		all_indices.erase(all_indices.begin() + index);
	}
	
	Interpreter ntpr{};
	for(int i = 3; i >= 0; i--) {
		sendCard(&ntpr, cards[indices[i]]);
	}
	
	return hidden == calculateHiddenCard(&ntpr);
}

bool sendCards_safe(u8* cards) {
	return cardsAreSorted(cards) && sendCards(cards);
}

void print5Cards(u8* cards) {
	for(int i = 0; i < 5; i++) {
		std::cout << (int) cards[i] << "\n";
	}
}

int main() {
	u8 max = 52;
	u8 test[5]{0, 1, 2, 3, 4};
	while(true) {
		if(!sendCards(test)) print5Cards(test);
		u8 i = 4;
		while(i >= 0 and test[i] == max + i - 4) i--;
		if(i < 0) return 0; // We are done.
		u8 newval = test[i];
		while(i < 5) {
			newval++;
			test[i] = newval;
			i++;
		}
	}
}

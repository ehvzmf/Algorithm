#include <stdio.h>

int main() {
	int n, temp, sum = 0; 
	int time[1001];
	
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - (i + 1); j++) {
			if (time[j] > time[j + 1]) {
				temp = time[j];
				time[j] = time[j + 1];
				time[j + 1] = temp;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			sum = sum + time[j]; 
		}
	}
	printf("%d", sum);

	return 0;
}

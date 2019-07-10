#include<iostream>
using namespace std;

void hanoi(int n, string pivote_inicial, string pivote_final, string pivote_auxiliar){
	if(n==1){
		cout << pivote_inicial << "->" << pivote_final << endl;
	}
	else{
		hanoi(n-1,pivote_inicial,pivote_auxiliar,pivote_final);
		cout << pivote_inicial << "->" << pivote_final << endl;
		hanoi(n-1,pivote_auxiliar,pivote_final,pivote_inicial);
	}
}

int main(){
	hanoi(4,"0","2","1");
	return 0;
}

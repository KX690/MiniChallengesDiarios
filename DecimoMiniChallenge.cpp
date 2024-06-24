#include <iostream>

using namespace std;


int numeros[5];
int aux=0;

int main(){


    for(int i=0;i<5;i++){
        cout<<"Introduzca un numero: ";
        cin>>numeros[i];
    }
    cout<<"Los numeros introducidos son: "<<endl;
    for(int i=0;i<5;i++){
        
        cout<<numeros[i]<< ",";
    }
    cout<<endl;
    for(int j=0;j<4;j++){
        for(int i=0;i<5;i++){
            if(numeros[i]>numeros[i+1]){
                aux=numeros[i];
                numeros[i]=numeros[i+1];
                numeros[i+1]=aux;

            }
        }
        

    }
    cout<<"Los numeros ordenados son: "<<endl;
    for(int i=0;i<5;i++){
        
        cout<<numeros[i]<< ",";
    }

}
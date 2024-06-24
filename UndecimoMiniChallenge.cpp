#include <iostream>
#include <string>

using namespace std;

string palabra;
bool b=false;

int main(){

    cout<<"Introduzca una palabra para saber si es un palindromo"<<endl;
    cin>>palabra;
    size_t aux2=palabra.length();

    for(int i=0;i<aux2;i++){
        if(palabra[i]!=palabra[aux2-i]){
            b=true;
            break;
        }

    }
    cout<<endl;
    if(!b){
        cout<<"Es un palindromo"<<endl;

    }else{
        cout<<"No es un palindromo"<<endl;
    }


}
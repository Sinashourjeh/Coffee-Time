#include <iostream>
#include <string>
using namespace std;

int main(){

int pass,action,balance,question,deposit,counts,withdrawal;
action=0;
balance=0;
deposit=0;
withdrawal=0;
counts=3;
string account_number;
account_number="0112030966600";
string account_name;
account_name="Canon Cleophace Ngirwa";
string mwisho;

logout_point:
cout <<"Welcome To HBT ATM v1.20\n";
wrong_point:
cout <<"Please enter your pin code: ";
cin>>pass;

while (pass==1990){
	system("cls");
	menu_point:
	cout <<"Welcome "<<account_name<<"\n";
		
	cout <<"1. Deposit            2. Withdrawal \n";
	cout <<"3. Check Balance      4. View Information \n";
	cout <<"5. Log Out\n";
	cout <<"Choose option: ";
	cin >>action;

	if (action==1){
		deposit_point:
		cout <<"Enter amount you wish to deposit: TSHs.";
		cin >>deposit;
		balance+=deposit;
		cout <<"Your amount is: TSHs."<<balance<<"\n";
		rudi_hapa1:
		cout <<"Do you want to deposit again? (1. Yes   2. No): \n";
		cout <<"Choose option: ";
		cin >>question;
		if (question==1){
			goto deposit_point;
		}//close selection 1
		else if (question==2){
			system("cls");
			goto menu_point;
		}//close selection 2
		else{
			cout <<"Wrong choice \n";
			goto rudi_hapa1;		
		}//wrong choice

	}//close deposit action

	else if (action==2){
		withdrawal_point:
		cout <<"Enter amount to withdrawal: TSHs.";
		cin>>withdrawal;

		if (balance<=1000){
			cout<<"Your balance is insufficient. Please deposit first \n";
			goto deposit_point;
		}//close if balance is less

		else if (balance-withdrawal<=0 || balance-withdrawal<=999){
			cout <<"You can not withdrawal this amount \n";
			goto withdrawal_point;
		}//close minimum withdrawal

		else if (withdrawal<=0){
			cout <<"You can not withdrawal this amount \n";
			goto withdrawal_point;
		}//close negative withdrawal

		else if (withdrawal>0){
			balance=balance-withdrawal;
			cout <<"\nYou have withdrawan: TSHs."<<withdrawal<<endl;
			cout <<"Your new balance is: TSHs."<<balance<<endl;
			rudi_hapa2:
			cout <<"Continue to withdrawal? (1. Yes   2. No): \n";
			cout <<"Choose option: ";
			cin >>question;
			if (question==1){
				goto withdrawal_point;
			}//close selection 1
			else if (question==2){
				system("cls");
				goto menu_point;
			}//close selection 2	
			else{
				cout <<"Wrong choice \n";
				goto rudi_hapa2;		
			}//wrong choice
		}//close correct withdrawal

		else {
			cout <<"You entered incorrect amount. Please try again \n";
			goto withdrawal_point;
		}//close incorrect withdrawal amount

	} //close withdrawal action

	else if (action==3){
		balance_point:
		cout <<"Your Balance is: TSHs."<<balance<<"\n";
		rudi_hapa3:
		cout <<"Do you want to check balance again? (1. Yes   2. No): \n";
		cout <<"Choose option: ";
		cin >>question;
		if (question==1){
			goto balance_point;
		}//close selection 1
		else if (question==2){
			system("cls");
			goto menu_point;
		} //close selection 2
		else{
			cout <<"Wrong choice \n";
			goto rudi_hapa3;		
		}//wrong choice
	} //close balance action

	else if (action==4){
		info_point:
		cout <<"Your Name is: "<<account_name<<"\n";
		cout <<"Your Account Number is: "<<account_number<<"\n";
		cout <<"Your Balance is: TSHs."<<balance<<"\n";
		rudi_hapa4:
		cout <<"Update information? (1. Yes   2. No): \n";
		cout <<"Choose option: ";
		cin >>question;
		if (question==1){
			system("cls");
			cout <<"You do not have privileges to change this. Contact your bank \n\n";
			goto info_point;
		}//close selection 1
		else if (question==2){
			system("cls");
			goto menu_point;
		} //close selection 2
		else{
			cout <<"Wrong choice \n";
			goto rudi_hapa4;		
		}//wrong choice
	} //close Account Information action

	else if (action==5){		
		cout <<"Goodbye. Thank you for using HBT ATM \n \n";
		system("cls");
		goto logout_point;
	} //close logout action

} //close for correct password

if (pass!=1990){
		counts=counts-1;
		cout <<"You have entered wrong password. Please try again \n";		
		cout <<counts<<" Attempts remained. \n";		
		if (counts<0){
			system("cls");
			cout <<"Too many attempts. System will shutdown now \n";
			cin >>mwisho;
		}//close if	
		else{
			goto wrong_point;
		}
	
}//close for wrong password



}//close main
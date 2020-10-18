#include<iostream>
using namespace std;
class count{
	public:
			void getData(int T)
			{
				int sum20=0,sum40=0,sum60=0,total;
				while(T!=0)
				{	
					int N;
					cout<<"Enter: ";
					cin>>N;
					sum20=(N*20)/100;
					sum40=(N*40)/100;
					sum60=(N*60)/100;
					total=(sum20+sum40+sum60);
					if(total>N)
					cout<<sum20<<ends<<sum40<<ends<<sum60;
					else
					cout<<"Fuk Off!!";
					T--;
				}
			}
};
main()
{
	count c;
	c.getData(2);
}

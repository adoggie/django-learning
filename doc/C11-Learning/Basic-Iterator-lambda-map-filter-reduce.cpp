
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <list>
#include <vector>
#include <tuple>
#include <iostream>
#include <stdexcept>
#include <numeric>
#include <iterator>

#include <sstream>

bool IsSpace(char x) { return x == ' '; }


typedef std::tuple< int,int> TwoInt;

int main() {
	std::cout << "Hello, World!" << std::endl;
	std::string name = "name is shanghai.";
//	auto itr = std::remove_if(name.begin(),name.end(),std::isspace);

	std::list<std::string> names={"cily","scott","eric"};

	std::string str2 = "Text with some  spaces";
	auto itr = std::remove_if(str2.begin(),  str2.end(),IsSpace);
//	str2.erase( itr, str2.end());
//	str2.erase(str2.find(' '));
	std::cout<< str2<< std::endl;
//
	std::for_each(itr,str2.end(),[](const unsigned char & ch){
		std::cout<< ch<< std::endl;
	});

	std::for_each(names.begin(),names.end(),[](const std::string& s){
		std::cout<<s<<std::endl;
	});

	TwoInt ti = std::make_tuple(1,2);
	ti = {2,3};
	std::cout<< std::get<0>(ti) <<std::endl;

	std::cout<< std::hex << 42 << '\n';


	std::vector<int> nums ={1,2,3};
	std::vector<int> nums_2 ;

	int result = std::accumulate(nums.begin(),nums.end(),100);


	std::stringstream ss;
	ss<<"0x" << std::hex << result << std::endl;

	std::cout<< ss.str() ;

	std::copy(nums.cbegin(),nums.cend(),std::back_inserter(nums_2));
	std::for_each(nums_2.begin(),nums_2.end(),[](const  int & v){
		std::cout<<std::hex<<v<<" ";
	});

	std::vector<int> nums_3 ;

	std::transform(nums.begin(),nums.end(),std::back_inserter(nums_3),[](const int & v){
		return v+100;
	});

	std::for_each(nums_3.begin(),nums_3.end(),[](const  int & v){
		std::cout<<std::dec<<v<<" ";
	});
	return 0;
}

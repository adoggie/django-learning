
std::string http_get(const std::string & url){
	std::cout<< "thread in http_get().."<<std::endl;
	std::this_thread::sleep_for(std::chrono::seconds(5));
//	std::this_thread::sleep_for(std::chrono::seconds(2));
	return "get succ..";
}

void test_async(void){
	std::cout<< "start.."<<std::endl;
	std::this_thread::sleep_for(std::chrono::seconds(2));
	std::future<std::string> f = std::async(http_get,"baidu.com");
//	std::cout<< "future result:"<< f.get() << std::endl;
	f.wait();
	std::cout<< "end.."<<std::endl;
}


void thread_promise( std::promise<std::string> & p ){
	std::this_thread::sleep_for(std::chrono::seconds(2));
	p.set_value("1000");
	std::puts("thread_promise exit..");
}


void test_promise(){
	std::promise<std::string> promise;
	std::thread thread(thread_promise,std::ref(promise) );
	auto f = promise.get_future();
	auto result = f.wait_for(std::chrono::seconds(5) );
	if (result == std::future_status::timeout){
		std::cout<< "wait timeout.."<<std::endl;
	}else if (result == std::future_status::ready){
		std::cout<<"result :"<< f.get() << std::endl;
	}
	thread.join();
}

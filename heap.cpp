#include <iostream>
#include <bits/stdc++.h>
using namespace std;

//min heap node
struct mhNode{
	char sym;
	int freq;
	mnNode *left
	mhNode *right 
	
	mhNode(char sym, int freq){
		left=NULL;
		right=NULL;
		this->sym=sym;
		this->freq;
  	}
};

//compare min nodes
int compare(mhNode *l, mhNode *r){
	if (l->freq > r->freq)
		return l->freq;
}




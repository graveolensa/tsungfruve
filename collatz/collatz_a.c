#include <stdlib.h>
#include <stdio.h>
#include <math.h>


int main(int argv, char *argc[])
{
  int i,length;
  int j,value;
  for(i=1;i<10000;i++)
    {
      value=i;
      length=0;
      while(value!=1)
	{
	  length=length+1;
	  if(div(value,2).rem==0)
	    {
	      value=value/2;
	    }
	  else
	    {
	      value=3*value+1;
	    }
	}
      printf("%d %d\n", i,length);
    }
  return 0;
}

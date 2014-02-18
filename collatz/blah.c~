#include <stdlib.h>
#include <stdio.h>
#include <math.h>



int number;
  
int count;
int newlength;
int maxvalue,length;
int newcount;
int lengthdiff;
int j;
int value;



int main(int argv, char *argc[])
{
  for(count=1;count<1000;count++)
    {
      value=count;    
      /* gather some data*/
      while(value!=1)
        {
	  printf("%d, ", value);
	  if(value>maxvalue)
	    {
	      maxvalue=value;
	    }
          if(div(value,2).rem==0)
            {
              value=value/2;
            }
          else
            {
              value=3*value+1;
            }
	
	}
      printf("%d\n ", value);
    }
  /*use gathered data */

  return 0;
}

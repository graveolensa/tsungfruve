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
          length=length+1;
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
    }
  /*use gathered data */
  printf("P2\n 200 1000\n %d\n", maxvalue);
  for(newcount=1;newcount<1001;newcount++)
    {
      value=newcount;    
      /* gather some data*/
      newlength=0;
      while(value!=1)
        {
          newlength=newlength+1;
	  printf("%d\n",value);
          if(div(value,2).rem==0)
            {
              value=value/2;
            }
          else
            {
              value=3*value+1;
            }
        }
      lengthdiff=200-newlength;
      for(j=0;j<lengthdiff;j++){printf("0\n");}
    }
  return 0;
}

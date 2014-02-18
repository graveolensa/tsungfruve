#include <stdlib.h>
#include <stdio.h>
#include <math.h>



int number;
int block[1001];
int count;
int newlength;
int maxvalue,length;
int newcount;
int lengthdiff;
int j;
int value;
int zerocount;
int newval;

int main(int argv, char *argc[])
{
  for(zerocount=0;zerocount<1001;zerocount++)
    {
      block[zerocount]=0;
    }


  for(count=1;count<1001;count++)
    {
      value=count;    
      /* gather some data*/
      while(value!=1)
        {
          block[count]=block[count]+1;
	
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


  printf("P2\n 200 1000\n %d\n", 1);


  for(newcount=1;newcount<1001;newcount++)
    {
      lengthdiff=200-block[newcount];
      for(j=0;j<lengthdiff;j++){printf("0\n");}
      newval=newcount;    
      while(newval!=1)
        {
          if(div(newval,2).rem==0)
            {
              newval=newval/2;
	      printf("1\n");
	    }
          else
            {
	      
	      newval=3*newval+1;
	      printf("0\n");
	    }
        }
     
     
    }
  return 0;
}

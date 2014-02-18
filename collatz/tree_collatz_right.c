#include <stdlib.h>
#include <stdio.h>
#include <math.h>



int number;
int length[1000];
int count;
int newlength;
int maxvalue;
int newcount;
int lengthdiff;
int j;
int value;
int itin;
int newcount;
int newvalue;
int fill;

int main(int argv, char *argc[])
{
  for(itin=1;itin<1000;itin++)
    {
      length[itin]=0;
    } 
  for(count=1;count<1000;count++)
    {
      value=count;    
      /* gather some data*/
      while(value!=1)
        {

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
	  length[count]=length[count]+1;
	}

    }
  /*use gathered data */

  for(newcount=1;newcount<1001;newcount++)
    {
      newvalue=newcount;    
      /* gather some data*/
      for(fill=0;fill<199-length[newcount];fill++)
	{
	  printf("0,");
	}
      while(newvalue!=1)
        {
	  printf("%d,", newvalue);
          if(div(newvalue,2).rem==0)
            {
              newvalue=newvalue/2;
            }
          else
            {
              newvalue=3*newvalue+1;
            }

	}
      printf("%d\n", newvalue);
    }

  return 0;
}

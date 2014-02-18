#include <stdlib.h>
#include <stdio.h>
#include <math.h>



int number;
int lengths[1000];  
int count;
int newlength;
int maxvalue,length;
int newcount;
int lengthdiff;
int j;
int value;
int initcount;


int main(int argv, char *argc[])
{
  for(initcount=1;initcount<1001;initcount++)
    {lengths[initcount]=0;}
 printf("lengths array zero filled\n");
  for(count=1;count<1001;count++)
    {
      value=count;    
      /* gather some data*/
 
     while(value!=1)
        {
          lengths[count]=lengths[count]+1;
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

  printf("initialization loops completed\n");
  /*use gathered data */
  printf("P2\n 200 1000\n %d\n", maxvalue);

  for(newcount=1;newcount<1001;newcount++)
    {
     for(j=0;j<lengths[newcount];j++){printf("0\n");} 
     value=newcount;   
      newlength=0;
      while(value!=1)
        {
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

    }
  return 0;
}

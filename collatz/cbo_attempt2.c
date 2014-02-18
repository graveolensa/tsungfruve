#include <stdlib.h>
#include <stdio.h>
#include <math.h>


int  next_collatz_number(int alpha)
{
  if(div(alpha,2).rem==0)
    {
      alpha = alpha/2;
    }
  else
    {
      alpha=(3*alpha)+1;
    }
  return alpha;
}

/* declare the image array */
int values[200][1000];
/* declare the lengths array */
int lengths[1000];
/* declare the initialization variables */
int initcount_a, initcount_b;
/* declare the value variable */
int value;
/* declare the work loop counter */
int i;
/* declare the lengthfinder loop counter */
int count_lengthfinder;
/* declare the value for the lengthfinder loop */
int val,q;
/* declare the printer variables */
int j,k;
/* declare the maximum value */
int maxvalue;
int main(int argv, char *argc[])
{
  /* fill the data array with zeroes */
  printf("IF YOU REACHED THIS POINT...\n");
  for(initcount_a=0;initcount_a<1000;initcount_a++)
    {
      /* while we're zeroing out the value array, let's also 
	 zero out the length array, just for kicks */
      lengths[initcount_a]=0;
      for(initcount_b=0;initcount_b<200;initcount_b++)
	{
	  values[initcount_b][initcount_a]=0;
	}
     /* initialize maxvalue */
      maxvalue = 0;
    }
  

  /* run the lengthfinder loop */
  for(count_lengthfinder=1;count_lengthfinder<1001;count_lengthfinder++)
    {
      val=count_lengthfinder;
      while(val!=1)
	{
	  /* get the maximum value (do it during the lengthfinder loop) */
	  if(val>maxvalue)
	    {
	      maxvalue=val;
	    }
	  else
	    {
	      maxvalue=maxvalue;
	    }
	  val=next_collatz_number(val);
	  lengths[count_lengthfinder-1]=lengths[count_lengthfinder-1]+1;
	}
    }
  printf("LENGTHFINDER LOOP COMPLETED\n");
  for(i=0;i<1000;i++)
    {
      /* get starting value from index */
      value=i;      
      /* STAGE A: reset starting position for filling data array. 
      /* begin the actual collatz loop 
	 note that I need to turn next_collatz_number() into
	 an actual function to improve the readability of the code */
      for(q=0;q<lengths[i];q++)
	{
	  values[200-lengths[i]+q][i]=value;
	  value=next_collatz_number(value);
	}
      /* stupid me. I thought I've have to fill the array with zeroes after
	 I populated it with collatz values. dumb dumb dumb. I can fill the array with
	 zeroes before actually running the loop */
    }
  /* all the values have been calculated. oh fuck. they're still wrong
     I actually need the length data in advance, so that I can know where
     to start the put the start of the run so that the ends line up */
  
  /* print the dimensions of the image */
  printf("P2\n200 1000\n%d\n",maxvalue);
  for(j=0;j<200;j++)
    {
      for(k=0;k<1000;k++)
	{
	  printf("%d\n", values[j][k]);
	}
    }

  return 0;
}

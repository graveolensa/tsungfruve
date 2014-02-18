#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int length[1000];
int next_collatz_number(int alpha)
{
  if(div(alpha,2).rem==0)
    {
      alpha = alpha / 2;
    }
  else
    {
      alpha = 3*alpha+1;
    }
  return alpha;
}


int zerocount;
int lfc,val_lfc;
int workloop,t,sval;

int main(int argv, char *argc[])
{

  for(zerocount=1;zerocount<1001;zerocount++)
    {
      length[zerocount-1]=0;
    }

  for(lfc=1;lfc<1001;lfc++)
    {
      /* initialize starting value of the hailstone numbers */
      val_lfc=lfc;
      while(val_lfc!=1)
	{
	  /* move to next hailstone number */
	  val_lfc=next_collatz_number(val_lfc);
	  /* add one to length */
	  length[lfc-1]+1;
	}
    }

  for(workloop=1;workloop<1001;workloop++)
    {
      for(t=0;t<(200-length[workloop-1]+1);t++)
	{
	  printf("0\n");
	}
      sval=workloop;
      while(sval!=1)
	{
	  printf("%d\n", sval);
	  /* move to next hailstone number */
	  sval=next_collatz_number(sval);
	}
      /* this just prints 1 and needs to be outside of the loop */
     
    }
  return 0;
}

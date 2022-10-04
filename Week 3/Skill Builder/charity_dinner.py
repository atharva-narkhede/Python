// You are using Java
import java.util.*;
class Main {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        int p=sc.nextInt();
        int g=sc.nextInt();
            int r=sc.nextInt();
            int o=sc.nextInt();
            int t=sc.nextInt();
            int a,b,c,d,i,j,k,l,x,m,count=0;
            a=t/p;
            b=t/g;
            c=t/r;
            d=t/o;
             //max times a loop can run
             m=a+b+c+d; //random value dp wanted
             for(i=0;i<=a;i++){
                for(j=0;j<=b;j++){
                    for(k=0;k<=c;k++){
                        for(l=0;l<=d;l++)
                        { if((i*p)+(j*g)+(k*r)+(l*o)==t)
                            {count++;
                                x=i+j+k+l;
                                if(x<m)
                                m=x;
                                System.out.println("# of PINK is "+i+" # of GREEN is "+j+" # of RED is "+k+"# of ORANGE is "+l);
                            }
                        }
                    }
                }
            }
            System.out.println("Total combinations is "+count);
            System.out.println("Minimum number of tickets to print is "+m);
        }
    }
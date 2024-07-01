import java.util.*;
//O(n),O(1)
class Solution{
    public static void main(String s[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++)
            a[i]=sc.nextInt();
        sc.close();
        int t,i=0,j=n-1;
        while(i<j){
            t=a[j];
            a[j]=a[i];
            a[i]=t;
            i++;
            j--;
        }
        for(i=0;i<n;i++)
            System.out.print(a[i]+" ");
    }
}

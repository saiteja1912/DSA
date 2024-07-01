import java.util.*;

class Solution{
    
    static int[] left_rotate_1(int a[],int n,int d){
        //O(n),O(n)
        int k=0;
        int[] b=new int[n];
        for(int i=d;i<n;i++){
            b[k++]=a[i];
        }
        for(int i=0;i<d;i++){
            b[k++]=a[i];
        }
        for(int i=0;i<n;i++)
            a[i]=b[i];
        return a;
    }
    
    //move each ele of arr one ele towards left and store first ele at last
    //perform this for d times
    static int[] left_rotate_2(int a[],int n,int d){
        //O(n*d),O(1)
        int t=0;
        for(int i=0;i<d;i++){
            t=a[0];
            for(int j=1;j<n;j++){
                a[j-1]=a[j];
            }
            a[n-1]=t;
        }
        return a;
    }
    
    static int[] reverse_part_of_arr(int a[],int i,int j){
        while(i<j){
            int t=a[j];
            a[j]=a[i];
            a[i]=t;
            i++;
            j--;
        }
        return a;
    }
    
    //reverse 1st d ele
    //reverse rest of ele
    //reverse entire array
    static int[] left_rotate_3(int a[],int n,int d){
        //O(n),O(1)
        a=reverse_part_of_arr(a,0,d-1);
        a=reverse_part_of_arr(a,d,n-1);
        a=reverse_part_of_arr(a,0,n-1);
        return a;
    }
    
    public static void main(String str[]){
        int n,d;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        d=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++)
            a[i]=sc.nextInt();
        //a=left_rotate_1(a,n,d);
        //a=left_rotate_2(a,n,d);
        a=left_rotate_3(a,n,d);
        for(int i=0;i<n;i++){
            System.out.print(a[i]+" ");
        }
        sc.close();
    }
}

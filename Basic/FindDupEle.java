//import java.io.*;
import java.util.*;

public class FindDupEle {

    static int[] sortArr(int arr[],int n){
        //sorting array using bubble sort
        for(int i=0;i<n-1;i++){
            for(int j=0;j<n-i-1;j++){
                if(arr[j]>arr[j+1]){
                    int t=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
            }
        }
        return arr;
    }

    static void printArr(int arr[],int n){
        for(int i=0;i<n;i++)
        System.out.print(arr[i]+" ");

        System.out.println();
    }

    static int findDupEle(int arr[],int n){
        for(int i=0;i<n-1;i++){
            if(arr[i]==arr[i+1])
                return arr[i];
        }
        return -1;
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Main. */
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++)
            arr[i]=sc.nextInt();
        arr=FindDupEle.sortArr(arr,n);
        //FindDupEle.printArr(arr,n);
        System.out.println(FindDupEle.findDupEle(arr,n));
        sc.close();

            
    }
}
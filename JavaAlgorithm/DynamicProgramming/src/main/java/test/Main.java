package test;

import java.util.ArrayList;
import java.util.Scanner;
    public class Main {
        public static void main(String[] args) {
            int[][] arr = new int[41][2];
            ArrayList<Integer> list = new ArrayList<>();
            Scanner scanner = new Scanner(System.in);
            int a = scanner.nextInt();
            for(int k = 0; k< a; k++) {
                int b = scanner.nextInt();
                list.add(b);
            }
            for(int j=0;j<list.size();j++){
                int n = list.get(j);

                arr[0] = new int[]{1, 0};
                arr[1] = new int[]{0, 1};

                for (int i = 2; i < n + 1; i++) {
                    arr[i] = new int[]{(arr[i - 1][0] + arr[i - 2][0]), (arr[i - 1][1] + arr[i - 2][1])};
                }
                System.out.println(arr[n][0]+" "+arr[n][1]);

            }
        }
    }
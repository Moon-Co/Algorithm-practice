package DPPractice;
import java.util.*;
class Solution {
    public int solution(int N, int number){
        List<Set<Integer>> countList = new ArrayList<>();
        //2차원 배열 생성. 리스트와 set리스트.
        for(int i =0; i<9; i++){
            countList.add(new HashSet<>());
        }//이 리스트 각각에도 중복이 없는 리스트 선언. HashSet = 중복이없는 리스트지만 탐색이
        //매우빠름.
        countList.get(1).add(N);
        //1번사용한거에는 그냥 N들어감.
        for(int i =2; i<9; i++){
            Set<Integer> countSet = countList.get(i);
            //countSet = countList에 있는 set배열들. 5 2개로 12만들기, 5 3개로 12만들기..

            for(int j=1; j<=i; j++) {
                Set<Integer> preSet = countList.get(j);
                Set<Integer> postSet = countList.get(i - j);
                //첫연산결과 (연산) 끝연산결과
                //결과랑 결과끼리
                for(int preNum : preSet){
                    for(int postNum : postSet){
                        countSet.add(preNum+postNum);
                        countSet.add(preNum-postNum);
                        countSet.add(preNum*postNum);
                        if(preNum!=0 && postNum !=0){
                            countSet.add(preNum/postNum);
                        }
                    }
                }
                countSet.add(Integer.parseInt(String.valueOf(N).repeat(i)));
                //55, 555이거를 먼저 넣고 시작한다.
            }
            //countList에 결과 나오는 순간 바로 멈춰서 그 숫자 출력!
            for(Set<Integer> sub : countList){
                if(sub.contains(number)){
                    return countList.indexOf(sub);
                }
            }
        }



        return -1;
    }

}
public class DPProblem1 {
    public static void main(String[] args) {
        Solution result = new Solution();
        System.out.println(result.solution(5,12));
    }
}

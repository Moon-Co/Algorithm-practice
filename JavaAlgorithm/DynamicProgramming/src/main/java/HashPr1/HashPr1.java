package HashPr1;
import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i = 0;
        for(i=0;i<completion.length;i++){
            if(!participant[i].equals(completion[i])){
                break;
            }
        }
        return participant[i];

    }
}
public class HashPr1 {
    public static void main(String[] args) {
        Solution slt = new Solution();
        String[] part = {"leo", "kiki", "eden"};
        String[] comple = {"eden", "kiki"};

        slt.solution(part,comple);
    }
}

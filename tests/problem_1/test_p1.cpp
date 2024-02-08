#include "/autograder/submission/problems/problem_1.cpp"

float p1Answer(float consumed_water) {
    float cost;
    // write your code here
    if(consumed_water <= 30)
        cost = 0.4*consumed_water;
    else if(consumed_water <= 50)
        cost = 0.4*30 + 0.12*(consumed_water-30);
    else if(consumed_water <= 60)
        cost = 0.4*30 + 0.12*20 + 1.4*(consumed_water-50);
    else
        cost = 0.4*30 + 0.12*20 + 1.4*10 + (consumed_water-60)*1.5;
    cost += 13;

    // do not change code bellow!
    return cost;
}

int main(void) {
    bool is_correct = false;
    float correct_answer;
    float student_answer;
    correct_answer = p1Answer(13.3);
    student_answer = problemSolution1(13.3);

    is_correct = (correct_answer == student_answer);

    return is_correct ? 1 : 0;
}

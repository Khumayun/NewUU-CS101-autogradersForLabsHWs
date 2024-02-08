float problemSolution1(float consumed_water) {
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

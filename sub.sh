#!/bin/sh

for i in {10,100,1000,10000}
do
    cd $i
    for j in {Eigen,MKL}
    do
        cd $j
        cp ../../run.sh .
        mkdir build
        cd build
        cmake -DCMAKE_CXX_COMPILER=icpc ../
        make
        mv a.out ../
        cd ../
        cd ../
    done
    cd ../
done

    

$fa=0.5;
$fs=0.5;
union(){
        translate(v=[-22.5, -22.5, 0]){
            cube(size=[45, 45, 8.9]);
        };
        translate(v=[0, 0, -15]){
            cylinder(h=23.9, d=37.8);
        };
    };
    translate(v=[0, 0, -15.5]){
        cylinder(h=24.9, d=31.799999999999997);
    };
    translate(v=[15.0, 15.0, 1]){
        cylinder(h=9.9, d=6.1);
    };
    translate(v=[-15.0, 15.0, 1]){
        cylinder(h=9.9, d=6.1);
    };
    translate(v=[15.0, -15.0, 1]){
        cylinder(h=9.9, d=6.1);
    };
    translate(v=[-15.0, -15.0, 1]){
        cylinder(h=9.9, d=6.1);
    };
    translate(v=[15.0, 15.0, -1]){
        cylinder(h=8.9, d=2.5);
    };
    translate(v=[-15.0, 15.0, -1]){
        cylinder(h=8.9, d=2.5);
    };
    translate(v=[15.0, -15.0, -1]){
        cylinder(h=8.9, d=2.5);
    };
    translate(v=[-15.0, -15.0, -1]){
        cylinder(h=8.9, d=2.5);
    };
};

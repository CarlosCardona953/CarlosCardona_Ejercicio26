
#include <iostream>
#include <fstream>
using namespace std;


void solve_equation_rgk(float t_init, float t_end, float delta_t, float omega, string filename);

int main(){
   
  //Para este caso tomamos el x inicial como 0 y el final como 30  
  float omega=1.0;
  solve_equation_rgk(0.0, 30, 0.1/omega, omega, "rgk_01.dat");
  solve_equation_rgk(0.0, 30, 0.01/omega, omega, "rgk_001.dat");
  solve_equation_rgk(0.0, 30, 1.0/omega, omega, "rgk_1.dat");
 
  return 0;
}

void solve_equation_rgk(float x_init, float x_end, float delta_x, float omega, string filename){
  float x=x_init;
  float y=1.0;
  float z=0;
  float y_old=y;
  float z_old=z;  
  float k0,k1,k2,k3,kp;
  float f = -omega*omega;
    
  ofstream outfile;
  outfile.open(filename);

  while(x<x_end){
      
    outfile << x << " " << y <<" " << z << endl;
        
      
    k0= y_old;
    k1= y_old + 0.5*k0*delta_x; 
    k2= y_old + 0.5*k1*delta_x; 
    k3= y_old + k2*delta_x; 
    
    kp= f*(k0+(k1*2)+(k2*2)+k3)/6;
    
    
    z = z_old + delta_x*kp;    
    y = y_old + delta_x * z_old;
    y_old=y;
    z_old=z;
    x = x + delta_x;
    
        
  
  }
  outfile.close();
}



#include <iostream>
#include <fstream>
using namespace std;


void solve_equation_rgk(float x_init, float x_end, float delta_x, float omega, string filename);
void solve_equation_euler(float x_init, float x_end, float delta_x, float omega, string filename);
//void solve_equation_leapfrog(float x_init, float x_end, float delta_x, float omega, string filename);

int main(){
   
  //Para este caso tomamos el x inicial como 0 y el final como 30  
  float omega=1.0;
  solve_equation_rgk(0.0, 10000.0, omega/2, omega, "rgk_01.dat");
  solve_equation_euler(0.0, 10000.0, omega/2, omega, "euler.dat");
  //solve_equation_leapfrog(0.0, 10000.0, omega/2, omega, "leapfrog.dat");
 
  return 0;
}



void solve_equation_rgk(float x_init, float x_end, float delta_x, float omega, string filename){
  float x=x_init;
  float y=1.0;
  float z=0.0;
  float y_old=y;
  float z_old=z;  
  float k0,k1,k2,k3,kp;
  float m0,m1,m2,m3,mp;
  float f = -omega*omega;
    
  ofstream outfile;
  outfile.open(filename);
    
    
      while(x<x_end){
      
    outfile << x << " " << y <<" " << z << endl;
    y_old=y;
    z_old=z;    
      
    k0= y_old*f;
    k1= (y_old + 0.5*k0*delta_x)*(f); 
    k2= (y_old + 0.5*k1*delta_x)*(f); 
    k3= (y_old + k2*delta_x)*(f); 
    
    kp= (k0+(k1*2)+(k2*2)+k3)/6;
    
    m0= z_old + f*delta_x*y_old;
    m1= z_old +((y_old + 0.5*k0*delta_x)*(delta_x)*f); 
    m2= z_old +((y_old + 0.5*k1*delta_x)*(delta_x)*f); 
    m3= z_old +((y_old + k2*delta_x)*(delta_x)*f); 
    
    mp= (m0+(m1*2)+(m2*2)+m3)/6;
    
    z = z_old + delta_x*kp;    
    y = y_old + delta_x*mp;
   
    x = x + delta_x;
    
        
  
  }
  outfile.close();
}

void solve_equation_euler(float x_init, float x_end, float delta_x, float omega, string filename){
  float x=x_init;
  float y=1.0;
  float z=0;
  float y_old=y;
  float z_old=z;  
  
  float f = -omega*omega;
    
  ofstream outfile;
  outfile.open(filename);
    
    
      while(x<x_end){
      
    outfile << x << " " << y <<" " << z << endl;
  
        
    z = z_old + delta_x*y_old*f;    
    y = y_old + delta_x*z_old;
   
    y_old=y;
    z_old=z;        
    x = x + delta_x;
    
        
  
  }
  outfile.close();
}

using System;
 
namespace Triangle
{
        abstract class Figure
    {
        public abstract double Square();
        public abstract double Per();
        public abstract double Median_X();
        public abstract double Median_Y();
        public abstract string Tip_S();
        public abstract double Ugol_A();
        public abstract double Ugol_B();
        public abstract double Ugol_C();
        public abstract string Tip_U();
    }
    class Triangle : Figure
    {
        
           // поля
        double Ax;
        double Ay;
        double Bx;
        double By;
        double Cx;
        double Cy;
       
        // свойства
        public double AX
        {
            get { return Ax; }
            set { Ax = value; }
        }
        public double AY
        {
            get { return Ay; }
            set { Ay = value; }
        }
             public double BX
        {
            get { return Bx; }
            set { Bx = value; }
        }
        public double BY
        {
            get { return By; }
            set { By = value; }
        }
             public double CX
        {
            get { return Cx; }
            set { Cx = value; }
        }
        public double CY
        {
            get { return Cy; }
            set { Cy = value; }
        }
 
        // конструктор
        public Triangle(double x1, double y1, double x2, double y2, double x3, double y3)
        {
            AX = x1;
            AY = y1;
            BX = x2;
            BY = y2;
            CX = x3;
            CY = y3;
        }
        
        // длины сторон
        public double Length(double x1, double y1, double x2, double y2 )
        {
            return Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2));
        }
        public double Length2(double x2, double y2, double x3, double y3)
        {
            return Math.Sqrt(Math.Pow(x3 - x2, 2) + Math.Pow(y3 - y2, 2));
        }
        public double Length3(double x1, double y1, double x3, double y3)
        {
            return Math.Sqrt(Math.Pow(x3 - x1, 2) + Math.Pow(y3 - y1, 2));
        }
 
        //периметр
        public override double Per()
        {
            return Length(AX,AY,BX,BY) + Length2(BX,BY,CX,CY) + Length3(AX,AY,CX,CY);
        }
        // площадь
        public override double Square()
        {
            double p = this.Per() / 2;
            return Math.Sqrt(p * (p - Length(AX,AY,BX,BY)) * (p - Length2(BX,BY,CX,CY)) * (p - Length3(AX,AY,CX,CY)));
        }
        public override double Median_X()
        {
            return ((AX+BX+CX)/3);
        }
        public override double Median_Y()
        {
            return ((AY+BY+CY)/3);
        }
        public override string Tip_S()
        {
            if ((Length(AX,AY,BX,BY)==Length2(BX,BY,CX,CY))&(Length(AX,AY,BX,BY)==Length3(AX,AY,CX,CY)))
            {
                return ("Треугольник равносторонний");
            }
            else if (((Length(AX,AY,BX,BY)==Length2(BX,BY,CX,CY))&(Length(AX,AY,BX,BY)!=Length3(AX,AY,CX,CY)))^((Length(AX,AY,BX,BY)==Length3(AX,AY,CX,CY))&(Length(AX,AY,BX,BY)!=Length2(BX,BY,CX,CY)))^((Length2(BX,BY,CX,CY)==Length3(AX,AY,CX,CY))&((Length2(BX,BY,CX,CY)!=Length(AX,AY,BX,BY)))))
            {
                return ("Треугольник равнобедренный");
            }
            else
            {
                return ("Треугольник разносторонний");
            }
        }
        public override double Ugol_A()
        {
            return (Math.Acos((Math.Pow(Length(AX,AY,BX,BY), 2)+Math.Pow(Length3(AX,AY,CX,CY),2)-Math.Pow(Length2(BX,BY,CX,CY),2))/(2*Math.Abs(Length(AX,AY,BX,BY))*Math.Abs(Length3(AX,AY,CX,CY))))*(180/Math.PI));
        }
        public override double Ugol_B()
        {
            return (Math.Acos((Math.Pow(Length(AX,AY,BX,BY), 2)-Math.Pow(Length3(AX,AY,CX,CY),2)+Math.Pow(Length2(BX,BY,CX,CY),2))/(2*Math.Abs(Length(AX,AY,BX,BY))*Math.Abs(Length2(BX,BY,CX,CY))))*(180/Math.PI));
        }
        public override double Ugol_C()
        {
            return (Math.Acos((Math.Pow(Length3(AX,AY,CX,CY),2)+Math.Pow(Length2(BX,BY,CX,CY),2)-Math.Pow(Length(AX,AY,BX,BY), 2))/(2*Math.Abs(Length2(BX,BY,CX,CY))*Math.Abs(Length3(AX,AY,CX,CY))))*(180/Math.PI));
        }
        public override string Tip_U()
        {
            if ((Ugol_A()<90)&(Ugol_B()<90)&(Ugol_C()<90))
            {
                return ("Треугольник остроугольный");
            }
             
            else if ((Ugol_A()==90)^(Ugol_B()==90)^(Ugol_C()==90))
            {
                return ("Треугольник прямоугольный");
            } 
            else 
            {
                return ("Треугольник тупоугольный");
            }

        }
    }
    class test
    {
        public static void Main()
        
        {   
            System.Console.WriteLine("Введите x1 =");
            double a1 = double.Parse(Console.ReadLine());
            System.Console.WriteLine("Введите y1 =");
            double a2 = double.Parse(Console.ReadLine());
            System.Console.WriteLine("Введите x2 =");
            double b1 = double.Parse(Console.ReadLine());
            System.Console.WriteLine("Введите y2 =");
            double b2 = double.Parse(Console.ReadLine());
            System.Console.WriteLine("Введите x3 =");
            double c1 = double.Parse(Console.ReadLine());
            System.Console.WriteLine("Введите y3 =");
            double c2 = double.Parse(Console.ReadLine());

            Figure f1;
            f1 = new Triangle(a1,a2,b1,b2,c1,c2);
            if ((f1.Square())!=0)
            {
                System.Console.WriteLine("Периметр треугольника =" + f1.Per());
                System.Console.WriteLine("Площадь треугольника =" + f1.Square());
                System.Console.WriteLine("Координаты точки пересечения медиан x=" + f1.Median_X()+" y= "+ f1.Median_Y());
                System.Console.WriteLine("Тип по сторонам: " + f1.Tip_S()+"  Тип по углам: "+ f1.Tip_U());
                System.Console.WriteLine("Угол а=: " + f1.Ugol_A()+"  Угол b=: " + f1.Ugol_B()+"  Угол c=: " + f1.Ugol_C());
            }
            else
            {
                System.Console.WriteLine("Невозможно постороить треугольник");
            }
        }
    }
}
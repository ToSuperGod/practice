#include "mainwidget.h"
#include <QPushButton>
MainWidget::MainWidget(QWidget *parent)
    : QWidget(parent)
{

    b1.setParent(this);
    b1.setText("close");
    b1.move(100,100);

    b2 = new QPushButton(this);
    b2->setText("lalala");

    connect(&b1, &QPushButton::pressed,this,&MainWidget::close);

    connect(b2,&QPushButton::released,this,&MainWidget::mySlot);
    connect(b2,&QPushButton::released,&b1,&QPushButton::hide);


    setWindowTitle("老大");
    b3.setParent(this);
    b3.setText("切换到子窗口");
    b3.move(50,50);

    //w.show();

    //处理子窗口信号
    connect()

    QPushButton *b5 = new QPushButton(this);
    b5->setText("Lambbda");
    int a=1,b=2;
    connect(b5,&QPushButton::released(),
            //= 把外部所有局部变量，类中所有成员一值传递   传进变量只读   修改加mutable
            //& 外部所有局部变量
            //this 类中所有
            // （）中可以传参
            [=]() mutable
    {
        b5->setText("fa");
        qDebug() << "111";
    })

}

void MainWidget::mySlot()
{
    b2->setText("123");
}
MainWidget::~MainWidget()
{

}

#include "subwidget.h"

subWidge::subWidge(QWidget *parent) : QWidget(parent)
{
    this->setWindowTitle("xiaodi");
    b4,setParent(this);
    b4.setText("切换到主窗口");

    connect(&b4,&QPushButton::clicked,this,&subWidge::sendSlot);
}

void subWidge::sendSlot()
{
    emit mySignal();
}

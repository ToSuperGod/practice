#ifndef SUBWIDGE_H
#define SUBWIDGE_H

#include <QWidget>
#include <QPushButton>
class subWidge : public QWidget
{
    Q_OBJECT
public:
    explicit subWidge(QWidget *parent = nullptr);
    void sendSlot();

signals:
    /*信号就是函数的声明，只需声明，无需定义*/
    void mySignal();

public slots:

private:
    QPushButton b4;
};

#endif // SUBWIDGE_H

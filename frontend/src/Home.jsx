import { Button, PageHeader, Tag, Layout, Row, Col, Menu, InputNumber, Typography, Alert, message, notification } from 'antd'
import { DownloadOutlined } from '@ant-design/icons'
import React, { useEffect, useState } from 'react'
import { StyleSheet, css } from 'aphrodite';
import axios from 'axios'
import ReactEcharts from 'echarts-for-react';

const { Header, Content, Footer } = Layout;
const { Text } = Typography;

const styles = StyleSheet.create({
  icon: {
    color: 'rgba(0,0,0,.25)',
  },
  title: {
    fontSize: '150%',
    color: 'white'
  }
});

const openNotification = () => {
  notification.open({
    message: '小组成员信息',
    description:
      '张俸铭 121037910013\n \
       董彦君 121037910037\n \
       程妍璇 121037910036\n \
       陈萌 121037910015\n \
       芮召普 121037910034',
    onClick: () => {
      console.log('Notification Clicked!');
    },
  });
};

const Home = () => {

  const temp_min = 20
  const temp_max = 30
  const humi_min = 30
  const humi_max = 50

  const [data, setData] = useState({
    temperature: 0,
    humidity: 0,
  })

  const [monitor, setMonitor] = useState({
    invade_indecator: 1
  })

  const tmpoption = {
    title: {
      text: '非法入侵统计'
    },
    tooltip: {
      trigger: 'axis',
      position: function (pt) {
        return [pt[0], '10%']
      },
      axisPointer: {
        animation: false
      }
    },
    xAxis: {
      type: 'time',
      splitLine: {
        show: false
      }
    },
    yAxis: {
      type: 'value',
      boundaryGap: [0, '100%'],
      splitLine: {
        show: false
      }
    },
    series: [
      {
        name: 'Data',
        type: 'line',
        showSymbol: false,
        data: null
      }
    ]
  }
  const [tempHistory, setTempHistory] = useState([])
  const [humiHistory, setHumiHistory] = useState([])
  const [monitorOption, setMonitorOption] = useState(tmpoption)
  const [timeLog, setTimeLog] = useState([])

  const [delta, setDelta] = useState(5000)
  const [deltaMonitor, setDeltaMonitor] = useState(500)
  const [deltaMonitorMonth, setDeltaMonitorMonth] = useState(3000)

  const [tmpDelta, setTmpDelta] = useState()

  const [date, setDate] = useState(new Date())

  const tempOption = {
    tooltip: {
      formatter: '{a} <br/>{b} : {c}℃'
    },
    series: [
      {
        name: '温度',
        type: 'gauge',
        detail: { formatter: '{value}℃' },
        min: -10,
        max: 30,
        axisLine: {          // 坐标轴线
          lineStyle: {       // 属性lineStyle控制线条样式
            color: [[0.3, '#63869e'], [0.45, '#91c7ae'], [1, '#c23531']]
          }
        },
        data: [{ value: data.temperature, name: '温度' }]
      }
    ]
  }

  const humiOption = {
    tooltip: {
      formatter: '{a} <br/>{b} : {c}%'
    },
    series: [
      {
        name: '湿度',
        type: 'gauge',
        detail: { formatter: '{value}%' },
        min: 0,
        max: 100,
        axisLine: {          // 坐标轴线
          lineStyle: {       // 属性lineStyle控制线条样式
            color: [[0.3, '#63869e'], [0.5, '#91c7ae'], [1, '#c23531']]
          }
        },
        data: [{ value: data.humidity, name: '湿度' }]
      }
    ]
  }

  const getOption = () => {
    return {
      xAxis: {
        name:'时间',
        type: 'category',
        data: []
      },
      yAxis: {
        name: '温度 /℃',
        type: 'value',
        data: []
      },
      series: [{
        data: tempHistory.map(item => item),
        type: 'line',
        itemStyle: {
          normal: {
            label: {
              show: tempHistory.length < 10 ? true : false
            }
          }
        }
      }]
    }
  }

  const getHumiOption = () => {
    return {
      xAxis: {
        name:'时间',
        type: 'category',
        data: []
      },
      yAxis: {
        name: '湿度 /%',
        type: 'value',
        data: []
      },
      series: [{
        data: humiHistory.map(item => item),
        type: 'line',
        itemStyle: {
          normal: {
            color: '#4682B4',
            label: {
              show: humiHistory.length < 10 ? true : false
            },
            lineStyle: {
              color: '#4682B4'
            }
          }
        }
      }]
    }
  }

  const getData = (url, data) => {
    return (
      axios.get(url, data).then(
        (response) => {
          return {
            temperature: Number(response.data.temperature).toFixed(2),
            humidity: Number(response.data.humidity)
          }
        }
      )
    )
  }

  const getMonitorData = (url, data) => {
    return (
      axios.get(url, data).then(
        (response) => {
          return {
            invade_indecator: Number(response.data.invade_indecator),
          }
        }
      )
    )
  }
  const handleMonitorHistory = async () => {
    try {
      let base = new Date() - 24*3600*1000*31;
      let oneDay = 24 * 3600 * 1000;
      let number = [];
      await getMonitorHistory('http://192.168.58.133:8000/api/monitor/month').then(res => {
        // console.log(res)
        for (let i = 0; i < 31; i++) {
          let now = new Date((base += oneDay));
          number.push([now, res[i]]);
        }
        const option = {
          title: {
            text: '非法入侵统计'
          },
          tooltip: {
            trigger: 'axis',
            position: function (pt) {
              return [pt[0], '10%']
            },
            axisPointer: {
              animation: false
            }
          },
          xAxis: {
            type: 'time',
            splitLine: {
              show: false
            }
          },
          yAxis: {
            type: 'value',
            boundaryGap: [0, '100%'],
            splitLine: {
              show: false
            }
          },
          series: [
            {
              name: 'Data',
              type: 'line',
              showSymbol: false,
              data: number
            }
          ]
        }
        setMonitorOption(option)
      })
    } catch (err) {
      console.log(err)
    }
  }

  
  const getMonitorHistory = (url, data) => {
    return (
      axios.get(url, data).then(
        (response) => {
          return response.data
        }
      )
    )
  }
  const handleClick = async () => {
    try {
      await getData('http://192.168.58.133:8000/api/temperature-humidity').then(res => {
        let newHistory = tempHistory
        newHistory.push(res.temperature)
        let newHumiHistory = humiHistory
        newHumiHistory.push(res.humidity)
        let newTimeLog = timeLog
        newTimeLog.push(new Date().toISOString())
        // console.log('date:', newTimeLog)
        setTempHistory(newHistory)
        setHumiHistory(newHumiHistory)
        setData(res)
      })
    } catch (err) {
      console.log(err)
    }
  }

  const handleMonitor = async () => {
    try {
      await getMonitorData('http://192.168.58.133:8000/api/monitor').then(res => {
        setMonitor(res)
      })
    } catch (err) {
      console.log(err)
    }
  }

  const changeInterval = (value) =>{
      setTmpDelta(value)
  }

  const handleInterval = () => {
    const regPos = /([1-9]?\d|100)$/
    if (regPos.test(tmpDelta)) {
      setDelta(tmpDelta* 1000)
      message.success('修改成功。')
    }
    else {
      message.error('修改失败：数据格式有误（1-100的整数）。')
    }
  }

  useEffect(() => {
    const id = setInterval(() => { handleClick() }, delta)
    const timer = setInterval(() => {
      setDate(new Date())
    }, 1000)
    return () => clearInterval(id)
  }, [delta])

  useEffect(() => {
    const id = setInterval(() => { handleMonitor() }, deltaMonitor)
    const timer = setInterval(() => {
      setDate(new Date())
    }, 1000)
    return () => clearInterval(id)
  }, [deltaMonitor])

  useEffect(() => {
    const id = setInterval(() => { handleMonitorHistory() }, deltaMonitorMonth)
    const timer = setInterval(() => {
      setDate(new Date())
    }, 1000)
    return () => clearInterval(id)
  }, [deltaMonitorMonth])

  const isWarning = () => {
    if (data.temperature > temp_max) {
      return 1
    }
    else if (data.temperature < temp_min) {
      return -1
    }
    return 0
  }

  const isHumiWarning = () => {
    if (data.humidity > humi_max) {
      return 1
    }
    else if (data.humidity < humi_min) {
      return -1
    }
    return 0
  }

  const isMonitorWarning = () => {
    return monitor.invade_indecator
  }

  const copyToClip = (content, message_) => {
    var aux = document.createElement("textarea");
    aux.value = content
    document.body.appendChild(aux);
    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
    if (message_ == null) {
      message.success("复制成功");
    } else {
      alert(message_);
    }
  }

  const handleDownloadLog = () => {
    let res = '时间戳\t温度\t湿度\t温度状态\t湿度状态\n'
    for(let i=0; i<timeLog.length; i++)
    {
      let time = timeLog[i].replace(/T/, ' ')
      time = time.replace(/Z/, ' ')
      let temp_status = tempHistory[i] > temp_max ? '温度过高' : tempHistory[i] < temp_min ? '温度过低' : '温度正常'
      let humi_status = humiHistory[i] > humi_max ? '湿度过高' : humiHistory[i] < humi_min ? '湿度过低' : '湿度正常'
      res += time + '\t' + tempHistory[i] + '\t' + humiHistory[i] + '\t' + temp_status + '\t' + humi_status + '\n'
    }
    copyToClip(res, null)
  }


  return (
    <div>
      <Layout className="layout">
        <Header style={{ display: 'flex', justifyContent: 'space-between' }}>
          <div className={css(styles.title)}>什么平台</div>
          <Menu theme="dark" mode="horizontal">
            <Menu.Item key="1" onClick={openNotification}>关于</Menu.Item>
          </Menu>
        </Header>
        <Content style={{ padding: '0 50px' }}>
          <PageHeader
            title={date.toLocaleTimeString()}
            subTitle='Vaccine cold chain warehouse management platform'
            className='site-page-header'
            tags={<Tag color='green'>Running</Tag>}
            extra={[
              <Text>自动拉取间隔(秒)</Text>,
              <InputNumber min={1} max={100} defaultValue={delta / 1000} onChange={changeInterval}></InputNumber>,
              <Button onClick={handleInterval}>修改间隔</Button>,
              <Button type="primary" onClick={handleClick}>读取数据</Button>,
            <Button onClick={handleDownloadLog} icon={<DownloadOutlined />}>复制数据到剪贴板</Button>
            ]}
          >
          </PageHeader>
          {
            isMonitorWarning() === 1 ?
            <Alert
              message="警告"
              description="有人非法闯入！"
              type="error"
              showIcon
              style={{ marginBottom: '1%', fontWeight: 'bold' }}
            /> : null
          }
          {
            isWarning() === 1 ?
              <Alert
                message="警告"
                description="当前获取的温度高于预警值。"
                type="warning"
                showIcon
                style={{ marginBottom: '1%', fontWeight: 'bold' }}
              /> : isWarning() === -1 ? <Alert
                message="警告"
                description="当前获取的温度低于预警值。"
                type="info"
                showIcon
                style={{ marginBottom: '1%', fontWeight: 'bold' }}
              /> : null
          }
          {
            isHumiWarning() === 1 ?
              <Alert
                message="警告"
                description="当前获取的湿度高于预警值。"
                type="warning"
                showIcon
                style={{ marginBottom: '1%', fontWeight: 'bold' }}
              /> : isHumiWarning() === -1 ? <Alert
                message="警告"
                description="当前获取的湿度低于预警值。"
                type="info"
                showIcon
                style={{ marginBottom: '1%', fontWeight: 'bold' }}
              /> : null
          }
          <Row>
            <Col span={12}>
              <ReactEcharts option={tempOption} style={{ height: '500px' }} />
            </Col>
            <Col span={12}>
              <ReactEcharts option={humiOption} style={{ height: '500px' }} />
            </Col>
          </Row>
          <Row>
            <Col span={12}>
              <ReactEcharts option={getOption()} style={{ height: '500px' }} />
            </Col>
            <Col span={12}>
              <ReactEcharts option={getHumiOption()} style={{ height: '500px' }} />
            </Col>
          </Row>
          <Row>
            <Col span={24}>
              <ReactEcharts option={monitorOption} style={{ height: '500px' }} />
            </Col>
          </Row>
        </Content>
        <Footer style={{ textAlign: 'center', backgroundColor: '#001529', color: 'white' }}>Created by Zhang Fengming, Dong Yanjun, Cheng Yanxuan, Chen Meng and Rui Shaopu © 2021 </Footer>
      </Layout>
    </div>
  )
}

export default Home

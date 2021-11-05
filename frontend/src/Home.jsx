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
      '施宇翔 120037910036\n 李嘉昊  120037910024\n陈江涛 120037910014\n王崇宇 120037910040\n王钰霄 020037910001',
    onClick: () => {
      console.log('Notification Clicked!');
    },
  });
};

const Home = () => {

  const temp_min = 2
  const temp_max = 8
  const humi_min = 30
  const humi_max = 50

  const [data, setData] = useState({
    temperature: 0,
    humidity: 0
  })

  const [tempHistory, setTempHistory] = useState([])
  const [humiHistory, setHumiHistory] = useState([])
  const [timeLog, setTimeLog] = useState([])

  const [delta, setDelta] = useState(5000)
  const deltaRef = React.createRef()
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
        axisLine: {            // 坐标轴线  
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
        axisLine: {            // 坐标轴线  
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

  const postData = (url, data) => {
    return (
      axios.get(url, data).then(
        (response) => {
          const datas = response.data.split(',')
          return {
            temperature: (Number(datas[0])- 0).toFixed(2) ,
            humidity: Number(datas[1])
          }
        }
      )
    )
  }

  const handleClick = async () => {
    try {
      await postData('http://10.166.18.198:8000/api/temperature-humidity').then(res => {
        let newHistory = tempHistory
        newHistory.push(res.temperature)
        let newHumiHistory = humiHistory
        newHumiHistory.push(res.humidity)
        let newTimeLog = timeLog
        newTimeLog.push(new Date().toISOString())
        console.log('date:', newTimeLog)
        setTempHistory(newHistory)
        setHumiHistory(newHumiHistory)
        setData(res)
      })
    } catch (err) {
      console.log(err)
    }

  }

  const handleInterval = () => {
    const regPos = /([1-9]?\d|100)$/
    if (regPos.test(deltaRef.current.rawInput)) {
      setDelta(deltaRef.current.rawInput * 1000)
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
          <div className={css(styles.title)}>疫苗冷链仓储管理平台</div>
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
              <InputNumber min={1} max={100} defaultValue={delta / 1000} ref={deltaRef}></InputNumber>,
              <Button onClick={handleInterval}>修改间隔</Button>,
              <Button type="primary" onClick={handleClick}>读取数据</Button>,
            <Button onClick={handleDownloadLog} icon={<DownloadOutlined />}>复制数据到剪贴板</Button>
            ]}
          >
          </PageHeader>
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
                style={{ fontWeight: 'bold' }}
              /> : isHumiWarning() === -1 ? <Alert
                message="警告"
                description="当前获取的湿度低于预警值。"
                type="info"
                showIcon
                style={{ fontWeight: 'bold' }}
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
        </Content>
        <Footer style={{ textAlign: 'center', backgroundColor: '#001529', color: 'white' }}>Created by Shi Yuxiang, Li Jiahao, Chen Jiangtao, Wang Chongyu and Wang Yuxiao © 2020 </Footer>
      </Layout>


    </div>
  )
}

export default Home
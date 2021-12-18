
control 'mongo service' do
  describe port(30163) do
    it { should be_listening }
  end
end

control 'mongo pod' do
  describe command('kubectl get pods | grep mongo | wc -l') do
    its('stdout') { should match /1/ }
  end
end


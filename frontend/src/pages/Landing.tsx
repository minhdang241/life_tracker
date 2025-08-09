import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Timer, Calendar, BarChart3, Target, BookOpen, TrendingUp } from "lucide-react";
import { Link } from "react-router-dom";

const Landing = () => {
  return (
    <div className="min-h-screen bg-background">
      {/* Hero Section */}
      <div className="relative overflow-hidden bg-gradient-to-br from-primary/5 via-secondary/5 to-accent/5">
        <div className="container mx-auto px-4 py-24">
          <div className="text-center space-y-8">
            <div className="space-y-4">
              <h1 className="text-5xl font-bold bg-gradient-to-r from-primary via-primary-glow to-secondary bg-clip-text text-transparent">
                TimeTracker Pro
              </h1>
              <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
                Track your time like a pro athlete. Gain insights into your productivity,
                manage goals, and reflect on your journey with powerful analytics.
              </p>
            </div>

            <div className="flex justify-center gap-4">
              <Button asChild size="lg" className="bg-gradient-to-r from-primary to-primary-glow">
                <Link to="/app">Start Tracking</Link>
              </Button>
              <Button asChild variant="outline" size="lg">
                <a href="#features">Learn More</a>
              </Button>
            </div>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div id="features" className="container mx-auto px-4 py-24">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold mb-4">Everything you need to optimize your time</h2>
          <p className="text-muted-foreground max-w-2xl mx-auto">
            Comprehensive time tracking with subjective data, goal management, and reflections
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <Card className="bg-gradient-to-br from-primary/5 to-primary/10 border-primary/20">
            <CardHeader>
              <Timer className="w-12 h-12 text-primary mb-4" />
              <CardTitle>Live Time Tracking</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Start/stop timer with categorization. Track Work, Training, Life Admin, and Rest
                with detailed subcategories and subjective ratings.
              </p>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-br from-secondary/5 to-secondary/10 border-secondary/20">
            <CardHeader>
              <Target className="w-12 h-12 text-secondary mb-4" />
              <CardTitle>Goal Management</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Set daily and weekly goals with subtasks. Track completion rates
                and see your progress in beautiful analytics dashboards.
              </p>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-br from-accent/5 to-accent/10 border-accent/20">
            <CardHeader>
              <BookOpen className="w-12 h-12 text-accent mb-4" />
              <CardTitle>Daily Reflections</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Write daily and weekly reflections to track your thoughts,
                insights, and progress over time.
              </p>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-br from-muted/5 to-muted/10 border-muted/20">
            <CardHeader>
              <Calendar className="w-12 h-12 text-muted-foreground mb-4" />
              <CardTitle>Daily Timeline</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                View your daily activities in a timeline format. Edit entries,
                add notes, and see how your focus, stress, and energy changed.
              </p>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-br from-primary/5 to-secondary/5 border-primary/20">
            <CardHeader>
              <BarChart3 className="w-12 h-12 text-primary mb-4" />
              <CardTitle>Advanced Analytics</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Compare weeks, months, and years. See completion rates,
                time distribution, and subjective data trends.
              </p>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-br from-secondary/5 to-accent/5 border-secondary/20">
            <CardHeader>
              <TrendingUp className="w-12 h-12 text-secondary mb-4" />
              <CardTitle>Performance Insights</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Track how activities affect your focus, stress, and energy levels.
                Optimize your schedule based on data-driven insights.
              </p>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* CTA Section */}
      <div className="bg-gradient-to-r from-primary/10 via-secondary/10 to-accent/10 py-24">
        <div className="container mx-auto px-4 text-center">
          <div className="space-y-8">
            <h2 className="text-3xl font-bold">Ready to take control of your time?</h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Join the ranks of high performers who track their time with precision and purpose.
            </p>
            <Button asChild size="lg" className="bg-gradient-to-r from-primary to-primary-glow">
              <Link to="/app">Start Your Journey</Link>
            </Button>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-card border-t py-12">
        <div className="container mx-auto px-4 text-center">
          <p className="text-muted-foreground">
            © 2024 TimeTracker Pro. Built for those who value their time.
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Landing;
